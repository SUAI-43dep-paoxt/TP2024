import caldav
from caldav import CalendarObjectResource
from caldav.lib.error import NotFoundError, AuthorizationError
from client.TaskManager.caldav_client.exceptions import CalendarNotFound, InvalidCredentials, TaskNotFound
from datetime import datetime, timedelta
from enum import Enum
from schemas import Task, Status


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
        # creator: Optional[str] = None
        # executor: Optional[str] = None
    )


class CalDavAdapter:

    def __init__(self, url: str, login: str, password: str):
        self.url = url
        self.login = login
        self.password = password

    def create_task(self, calendar_name: str, task: Task):
        try:
            with caldav.DAVClient(url=self.url, username=self.login, password=self.password) as client:
                principal = client.principal()

                try:
                    calendar = principal.calendar(calendar_name)
                except NotFoundError:
                    raise CalendarNotFound

                calendar.save_todo(
                    summary=task.title,
                    description=task.description,
                    dtstart=task.start_time,
                    due=task.end_time,
                    categories=task.tags,
                    priority=task.priority,
                    status=map_to_caldavstatus(task.status).value)

        except AuthorizationError:
            raise InvalidCredentials

    def get_tasks(self, calendar_name: str, from_date: datetime, to_date: datetime) -> list[Task]:
        try:
            with caldav.DAVClient(url=self.url, username=self.login, password=self.password) as client:
                principal = client.principal()

                try:
                    calendar = principal.calendar(calendar_name)
                except NotFoundError:
                    raise CalendarNotFound

                result = []

                todos = calendar.search(start=from_date, end=to_date, todo=True)
                for todo in todos:
                    result.append(map_to_task(todo))

                return result

        except AuthorizationError:
            raise InvalidCredentials

    def get_task(self, calendar_name: str, uid: str):
        try:
            with caldav.DAVClient(url=self.url, username=self.login, password=self.password) as client:
                principal = client.principal()

                try:
                    calendar = principal.calendar(calendar_name)
                except NotFoundError:
                    raise CalendarNotFound

                try:
                    todo = calendar.todo_by_uid(uid)
                except NotFoundError:
                    raise TaskNotFound

                return map_to_task(todo)

        except AuthorizationError:
            raise InvalidCredentials

    def update_task(self, calendar_name: str, uid: str, task: Task):
        try:
            with caldav.DAVClient(url=self.url, username=self.login, password=self.password) as client:
                principal = client.principal()

                try:
                    calendar = principal.calendar(calendar_name)
                except NotFoundError:
                    raise CalendarNotFound

                try:
                    todo = calendar.todo_by_uid(uid)
                except NotFoundError:
                    raise TaskNotFound

                todo.icalendar_component["summary"] = task.title
                todo.icalendar_component["description"] = task.description
                todo.icalendar_component["dtstart"].dt = task.start_time
                todo.icalendar_component["due"].dt = task.end_time
                todo.icalendar_component["categories"] = task.tags
                todo.icalendar_component["priority"] = task.priority
                todo.icalendar_component["status"] = map_to_caldavstatus(task.status).value

                todo.save()

        except AuthorizationError:
            raise InvalidCredentials

    def delete_task(self, calendar_name: str, uid: str):
        try:
            with caldav.DAVClient(url=self.url, username=self.login, password=self.password) as client:
                principal = client.principal()

                try:
                    calendar = principal.calendar(calendar_name)
                except NotFoundError:
                    raise CalendarNotFound

                try:
                    todo = calendar.todo_by_uid(uid)
                except NotFoundError:
                    raise TaskNotFound

                todo.delete()

        except AuthorizationError:
            raise InvalidCredentials
