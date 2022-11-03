import math
from datetime import datetime
from typing import Any, List


def get_current_time_iso_format():
    return datetime.now().astimezone().isoformat(timespec="milliseconds")


def print_object(obj: Any):
    tmp = vars(obj)
    for f in tmp:
        if not f.startswith("__"):
            print(f"{f}: {tmp[f]}")


def divide_by_batch_size(input_list: List[Any], batch_size: int) -> List[List[Any]]:
    num_batches = math.ceil(len(input_list) / int(batch_size))
    return [
        input_list[batch_size * i : batch_size * (i + 1)] for i in range(num_batches)
    ]
