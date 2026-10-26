"""可修改的小测试示例：另选输入，保留自己的预期与解释。

测试通过参数接收课程 fixture，--impl 才能切换候选实现。
不要直接 from operations import pop_last 绕过这个开关。
"""

import numpy as np
import pytest


def test_my_pop_example(pop_last):
    items = [7, 4]

    result = pop_last(items)

    assert result == 4
    assert items == [7]


def test_my_pop_mixed_values(pop_last):
    items = [0, 3, 3, -2, 5]

    result = pop_last(items)

    assert result == 5
    assert items == [0, 3, 3, -2]


@pytest.mark.parametrize("container", ("list", "array"))
def test_my_positive_squares_mixed_values(positive_squares, container):
    initial = [0, 3, 3, -2, 5]
    values = initial.copy() if container == "list" else np.array(initial, dtype=int)
    before = values.copy()

    result = positive_squares(values)

    assert isinstance(result, list)
    assert result == [9, 9, 25]
    assert result is not values
    if container == "list":
        assert values == before
    else:
        np.testing.assert_array_equal(values, before)


def test_my_positive_square_map_keeps_key_order(positive_square_map):
    record = {"z": 3, "zero": 0, "a": 3, "minus": -2, "m": 5}
    before = record.copy()

    result = positive_square_map(record)

    assert isinstance(result, dict)
    assert result == {"z": 9, "a": 9, "m": 25}
    assert list(result) == ["z", "a", "m"]
    assert result is not record
    assert record == before
    assert list(record) == list(before)
