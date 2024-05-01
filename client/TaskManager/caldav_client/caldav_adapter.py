import caldav
from caldav import CalendarObjectResource
from caldav.lib.error import NotFoundError, AuthorizationError
from client.TaskManager.caldav_client.exceptions import CalendarNotFound, InvalidCredentials
from datetime import datetime, timedelta
from enum import Enum
from schemas import Task, Status


class CalDavStatus(Enum):
    needs_action = 'NEEDS-ACTION'
    in_progress = 'IN-PROCESS'
    completed = 'COMPLETED'
    cancelled = 'CANCELLED'


def get_status_from_caldavstatus(caldavstatus: CalDavStatus) -> Status:
    match caldavstatus:
        case CalDavStatus.needs_action:
            return Status.todo
        case CalDavStatus.in_progress:
            return Status.in_progress
        case CalDavStatus.completed:
            return Status.done
        case CalDavStatus.cancelled:
            return Status.cancelled


def get_caldavstatus_from_status(status: Status) -> CalDavStatus:
    match status:
        case Status.todo:
            return CalDavStatus.needs_action.value
        case Status.in_progress:
            return CalDavStatus.in_progress.value
        case Status.done:
            return CalDavStatus.completed.value
        case Status.cancelled:
            return CalDavStatus.cancelled.value


def get_task_from_todo(todo: CalendarObjectResource) -> Task:
    return Task(
        uid=str(todo.icalendar_component["uid"]),
        title=str(todo.icalendar_component["summary"]),
        description=str(todo.icalendar_component["description"]),
        create_time=todo.icalendar_component["dtstamp"].dt,
        start_time=todo.icalendar_component["dtstart"].dt,
        end_time=todo.icalendar_component["due"].dt,
        tags=[str(tag) for tag in todo.icalendar_component["categories"].cats],
        status=get_status_from_caldavstatus(CalDavStatus(str(todo.icalendar_component["status"]))),
        priority=int(todo.icalendar_component["priority"]),
        # creator: Optional[str] = None
        # executor: Optional[str] = None
    )


class CalDavAdapter:

    def __init__(self, url: str, login: str, password: str):
        self.url = url
        self.login = login
        self.password = password

    def create_task(self, task: Task):
        try:
            with caldav.DAVClient(url=self.url, username=self.login, password=self.password) as client:
                principal = client.principal()

                try:
                    calendar = principal.calendar('Test tasklist')
                except NotFoundError:
                    raise CalendarNotFound

                calendar.save_todo(
                    summary=task.title,
                    description=task.description,
                    dtstart=task.start_time,
                    due=task.end_time,
                    categories=task.tags,
                    priority=task.priority,
                    status=get_caldavstatus_from_status(task.status))

        except AuthorizationError:
            raise InvalidCredentials

    def get_tasks(self, from_date: datetime, to_date: datetime) -> list[Task]:
        try:
            with caldav.DAVClient(url=self.url, username=self.login, password=self.password) as client:
                principal = client.principal()

                try:
                    calendar = principal.calendar('Test tasklist')
                except NotFoundError:
                    raise CalendarNotFound

                result = []

                todos = calendar.search(start=from_date, end=to_date, todo=True)
                for todo in todos:
                    result.append(get_task_from_todo(todo))

                return result

        except AuthorizationError:
            raise InvalidCredentials
