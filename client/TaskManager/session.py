import json
from pathlib import Path

from pip._internal.network import session

from invite_code.schemas import InviteCode


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SessionStorage(metaclass=Singleton):
    sessions_folder_name = ".calendar-sessions"

    def __init__(self):
        self._sessions: dict[str, InviteCode] = {}

        home_path = Path.home()
        self._sessions_path = home_path / self.sessions_folder_name
        self._sessions_path.mkdir(exist_ok=True)

        for filename in self._sessions_path.glob("*.json"):
            with open(filename, "r") as session_file:
                invite_code = self._sessions[filename.stem] = InviteCode(**json.load(session_file))
                self._sessions[invite_code.project_name] = invite_code

    def add(self, invite_code: InviteCode) -> None:
        self._sessions[invite_code.project_name] = invite_code

        with open(self.__get_session_file_name(invite_code), "w", encoding="utf-8") as file:
            file.write(invite_code.model_dump_json())

    @property
    def sessions(self) -> dict[str, InviteCode]:
        return self._sessions

    def __get_session_file_name(self, invite_code: InviteCode) -> str:
        return str(
            self._sessions_path
            / f'{invite_code.project_name}-{hash(invite_code.person.email)}.json'
        )
