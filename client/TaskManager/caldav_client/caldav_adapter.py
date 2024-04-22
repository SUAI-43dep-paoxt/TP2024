import caldav
from caldav.lib.error import NotFoundError, AuthorizationError
from client.TaskManager.caldav_client.exceptions import CalendarNotFound, InvalidCredentials
from datetime import datetime, timedelta
from schemas import Task, CalDavStatus, Status


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
                    status=self.get_caldav_status_from_entity(task.status))

        except AuthorizationError:
            raise InvalidCredentials

    def get_caldav_status_from_entity(self, status: Status) -> CalDavStatus:
        match status:
            case Status.todo:
                return CalDavStatus.needs_action.value
            case Status.in_progress:
                return CalDavStatus.in_progress.value
            case Status.done:
                return CalDavStatus.completed.value
            case Status.cancelled:
                return CalDavStatus.cancelled.value
