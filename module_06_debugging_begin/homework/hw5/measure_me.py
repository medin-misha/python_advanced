"""
Каждый лог содержит в себе метку времени, а значит, правильно организовав логирование,
можно отследить, сколько времени выполняется функция.

Программа, которую вы видите, по умолчанию пишет логи в stdout. Внутри неё есть функция measure_me,
в начале и в конце которой пишется "Enter measure_me" и "Leave measure_me".
Сконфигурируйте логгер, запустите программу, соберите логи и посчитайте среднее время выполнения функции measure_me.
"""
import logging
import random
from typing import List
from datetime import datetime as dt

logger = logging.getLogger(__name__)




def calculate_program_runtime(logs) -> str:

    time:dict = {
        "startTime":None,
        "endTime":None
    }

    for log in logs:

        log_parts = log.split(" | ")

        #dt.strptime переводит строковый формат времени в формат datatime
        log_time = dt.strptime(
            log_parts[0],
            "%Y-%m-%d %H:%M:%S,%f"
        )

        log_message = log_parts[1]


        match time["startTime"]:
            case None:
                time["startTime"] = log_time
        match log_message.strip():
            case "Leave measure_me":
                time["endTime"] = log_time
                break


    if time["startTime"] is None or time["endTime"] is None:
        return None

    runtime = time["endTime"] - time["startTime"]
    return f"программа работала {runtime.total_seconds()}s"

def get_data_line(sz: int) -> List[int]:
    try:
        logger.debug("Enter get_data_line")
        return [random.randint(-(2 ** 31), 2 ** 31 - 1) for _ in range(sz)]
    finally:
        logger.debug("Leave get_data_line")


def measure_me(nums: List[int]) -> List[List[int]]:
    logger.debug("Enter measure_me")
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        logger.debug(f"Iteration {i}")
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]
        if i == 0 or nums[i] != nums[i - 1]:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    logger.debug(f"Found {target}")
                    results.append([nums[i], nums[left], nums[right]])
                    logger.debug(
                        f"Appended {[nums[i], nums[left], nums[right]]} to result"
                    )
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    logger.debug(f"Increment left (left, right) = {left, right}")
                    left += 1
                else:
                    logger.debug(f"Decrement right (left, right) = {left, right}")

                    right -= 1

    logger.debug("Leave measure_me")

    return results


if __name__ == "__main__":


    logging.basicConfig(
        level="DEBUG",
        filename="measure_me.log",
        format="%(asctime)s | %(message)s"
    )

    for it in range(15):
        data_line = get_data_line(10)
        measure_me(data_line)

    with open("measure_me.log") as logsFile:
        print(calculate_program_runtime(logsFile))