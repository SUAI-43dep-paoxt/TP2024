import time
import multiprocessing as mp
from datetime import datetime, timedelta

from caldav_client.caldav_adapter import CalDavAdapter
from caldav_client.schemas import Task, UpdateTask
from caldav_client import tags


def _notification_worker(
    caldav_adapter: CalDavAdapter,
    executor: str,
    output_queue: mp.Queue,
    period: timedelta,
) -> None:
    while True:
        time.sleep(period.total_seconds())

        tasks: list[Task] = list(
            filter(
                lambda t: t.executor == executor and not t.informed,
                caldav_adapter.get_tasks(from_date=datetime.now(), to_date=datetime.now() + timedelta(hours=24)),
            ),
        )

        for task in tasks:
            new_tags = task.tags + [tags.INFORMED]
            print(new_tags)
            caldav_adapter.update_task(task.uid, UpdateTask(tags=new_tags))
            output_queue.put_nowait(task)


def run_notification_worker(
    caldav_adapter: CalDavAdapter,
    executor: str,
    period: timedelta = timedelta(minutes=5),
) -> mp.Queue:
    output_queue = mp.Queue()
    process = mp.Process(target=_notification_worker, args=(caldav_adapter, executor, output_queue, period))
    process.start()
    return output_queue
