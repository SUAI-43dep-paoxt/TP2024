from datetime import datetime
from enum import Enum

import caldav
import icalendar.prop
from caldav import CalendarObjectResource
from caldav.lib.error import AuthorizationError, NotFoundError

from client.TaskManager.caldav_client.exceptions import CalendarAlreadyExists, CalendarNotFound, InvalidCredentials, TaskNotFound
from client.TaskManager.caldav_client.schemas import Status, Task, UpdateTask


class CalDavStatus(Enum):
    needs_action = 'NEEDS-ACTION'
    in_progress = 'IN-PROCESS'
    completed = 'COMPLETED'
    cancelled = 'CANCELLED'


def map_to_caldavstatus(status: Status) -> CalDavStatus:
    match status:
        case Status.todo:
            return CalDavStatus.needs_action
        case Status.in_progress:
            return CalDavStatus.in_progress
        case Status.done:
            return CalDavStatus.completed
        case Status.cancelled:
            return CalDavStatus.cancelled


def map_to_status(caldavstatus: CalDavStatus) -> Status:
    match caldavstatus:
        case CalDavStatus.needs_action:
            return Status.todo
        case CalDavStatus.in_progress:
            return Status.in_progress
        case CalDavStatus.completed:
            return Status.done
        case CalDavStatus.cancelled:
            return Status.cancelled


def map_to_task(todo: CalendarObjectResource) -> Task:

    ics = str(todo.icalendar_component["ics"])
    fields = ics.split(':')

    creator = fields[0]
    executor = None
    if len(fields) > 1:
        executor = fields[1]

    return Task(
        uid=str(todo.icalendar_component["uid"]),
        title=str(todo.icalendar_component["summary"]),
        description=str(todo.icalendar_component["description"]),
        create_time=todo.icalendar_component["dtstamp"].dt,
        start_time=todo.icalendar_component["dtstart"].dt,
        end_time=todo.icalendar_component["due"].dt,
        tags=[str(tag) for tag in todo.icalendar_component["categories"].cats],
        status=map_to_status(CalDavStatus(str(todo.icalendar_component["status"]))),
        priority=int(todo.icalendar_component["priority"]),
        creator=creator,
        executor=executor
    )


class CalDavAdapter:

    @staticmethod
    def create_calendar(url: str, login: str, password: str, name: str):
        try:
            with caldav.DAVClient(url=url, username=login, password=password) as client:
                principal = client.principal()

                calendars = principal.calendars()
                for calendar in calendars:
                    if calendar.name == name:
                        raise CalendarAlreadyExists

                principal.make_calendar(name=name)

        except AuthorizationError:
            raise InvalidCredentials

    def __init__(self, url: str, login: str, password: str, calendar_name: str):
        self.url = url
        self.login = login
        self.password = password
        self.calendar_name = calendar_name

    def create_task(self, task: Task):
        try:
            with caldav.DAVClient(url=self.url, username=self.login, password=self.password) as client:
                principal = client.principal()

                try:
                    calendar = principal.calendar(self.calendar_name)
                except NotFoundError:
                    raise CalendarNotFound

                ics = task.creator if task.executor is None else f'{task.creator}:{task.executor}'
                print(map_to_caldavstatus(task.status))
                calendar.save_todo(
                    summary=task.title,
                    description=task.description,
                    dtstart=task.start_time,
                    due=task.end_time,
                    categories=task.tags,
                    priority=task.priority,
                    status=CalDavStatus.needs_action.value,
                    # status=map_to_caldavstatus(task.status).value,
                    ics=ics)

        except AuthorizationError:
            raise InvalidCredentials

    def get_tasks(self, from_date: datetime, to_date: datetime) -> list[Task]:
        try:
            with caldav.DAVClient(url=self.url, username=self.login, password=self.password) as client:
                principal = client.principal()

                try:
                    calendar = principal.calendar(self.calendar_name)
                except NotFoundError:
                    raise CalendarNotFound

                result = []

                todos = calendar.search(start=from_date, end=to_date, todo=True)
                for todo in todos:
                    result.append(map_to_task(todo))

                return result

        except AuthorizationError:
            raise InvalidCredentials

    def get_task(self, uid: str):
        try:
            with caldav.DAVClient(url=self.url, username=self.login, password=self.password) as client:
                principal = client.principal()

                try:
                    calendar = principal.calendar(self.calendar_name)
                except NotFoundError:
                    raise CalendarNotFound

                try:
                    todo = calendar.todo_by_uid(uid)
                except NotFoundError:
                    raise TaskNotFound

                return map_to_task(todo)

        except AuthorizationError:
            raise InvalidCredentials

    def update_task(self, uid: str, task: UpdateTask):
        try:
            with caldav.DAVClient(url=self.url, username=self.login, password=self.password) as client:
                principal = client.principal()

                try:
                    calendar = principal.calendar(self.calendar_name)
                except NotFoundError:
                    raise CalendarNotFound

                try:
                    todo = calendar.todo_by_uid(uid)
                except NotFoundError:
                    raise TaskNotFound

                if task.title is not None:
                    todo.icalendar_component["summary"] = task.title
                if task.description is not None:
                    todo.icalendar_component["description"] = task.description
                if task.start_time is not None:
                    todo.icalendar_component["dtstart"].dt = task.start_time
                if task.end_time is not None:
                    todo.icalendar_component["due"].dt = task.end_time
                if task.tags is not None:
                    todo.icalendar_component["categories"] = icalendar.prop.vCategory(task.tags)
                if task.priority is not None:
                    todo.icalendar_component["priority"] = task.priority
                if task.status is not None:
                    # todo.icalendar_component["status"] = map_to_caldavstatus(task.status).value
                    todo.icalendar_component["status"] = CalDavStatus.needs_action.value
                if task.executor is not None:
                    ics = str(todo.icalendar_component["ics"])
                    fields = ics.split(':')
                    creator = fields[0]
                    todo.icalendar_component["ics"] = f'{creator}:{task.executor}'

                todo.save()

        except AuthorizationError:
            raise InvalidCredentials

    def delete_task(self, uid: str):
        try:
            with caldav.DAVClient(url=self.url, username=self.login, password=self.password) as client:
                principal = client.principal()

                try:
                    calendar = principal.calendar(self.calendar_name)
                except NotFoundError:
                    raise CalendarNotFound

                try:
                    todo = calendar.todo_by_uid(uid)
                except NotFoundError:
                    raise TaskNotFound

                todo.delete()

        except AuthorizationError:
            raise InvalidCredentials
