import random


class HapakIsNotWorkingException(Exception):
    pass


def run_darwin_mission(task_id):
    # type: (int) -> str
    """
    DONT ALTER THIS FUNCTION!
    A function meant to be a totally accurate representation of running
    darwin tasks.
    """
    if random.randint(0, 10) > 5:
        msg = "The 847th system linking pasten to pasten via carrier piegons is offline. Please try again!"
        raise HapakIsNotWorkingException(msg)
    return "Darwin Task {} finisehd running successfully!".format(task_id)


def main():
    # type: () -> None
    """
    A function meant to be a totally accurate representation of hapak
    work.
    """
    missions_to_run = list(range(100))
    while missions_to_run:
        task_id = missions_to_run.pop(0)
        try:
            run_darwin_mission(task_id)
        except HapakIsNotWorkingException:
            missions_to_run.append(task_id)


if __name__ == "__main__":
    main()
