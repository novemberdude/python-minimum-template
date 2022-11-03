from typing import List

import pytest
from src.common_utils.utils import divide_by_batch_size


@pytest.mark.parametrize(
    "input_list, batch_size, expected_result",
    [
        ([1, 2, 3, 4,  5], 2, [[1, 2], [3, 4], [5]]),
        ([1, 2, 3, 4,  5], 5, [[1, 2, 3, 4, 5]]),
        ([1, 2, 3, 4,  5], 6, [[1, 2, 3, 4, 5]]),
        ([1, 2, 3, 4,  5], 1, [[1], [2], [3], [4], [5]]),
        # ([], [3], []),
    ],
)
def test_divide_by_batch_size(input_list: List[str], batch_size: int, expected_result):
    output = divide_by_batch_size(input_list, batch_size)
    assert output == expected_result
