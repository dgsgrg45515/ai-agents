# W5 必做验收记录

本次只实现三道基础题。预测由 Agent 按题意在实现前写下，供本人运行并核对；不代替本人理解与解释。

## 事前预测

| 调用 | 返回结果 | 调用后的原输入 |
| --- | --- | --- |
| `pop_last([0, 3, 3, -2, 5])` | `5` | `[0, 3, 3, -2]` |
| `positive_squares([0, 3, 3, -2, 5])` | `[9, 9, 25]` | 保持不变；一维整数数组同样如此 |
| `positive_square_map({"z": 3, "zero": 0, "a": 3, "minus": -2, "m": 5})` | `{"z": 9, "a": 9, "m": 25}` | 键、值和顺序均保持不变 |

正式题目只保留大于零的项，重复项不去重。`pop_last` 同时修改原列表并返回末项，另两题创建新容器。

## Notebook 跟练

`practice.ipynb` 保存必做示例与八处微练习的事前预测和实际输出。教师原始 `demo.ipynb` 用于对照。

已运行 19 个代码 cell，八处微练习的实际结果均符合事前预测。练习中将 `> 0` 改为 `>= 0` 会保留零；正式基础题仍使用 `> 0`。

## 实际验收

环境：WSL，Python **3.12.14**，NumPy **2.5.4**，解释器位于本周 `week-05/.venv/bin/python`。依赖使用原 `uv.lock`，通过 `uv sync --locked` 安装。

| 验收对象 | 实际结果 | 含义 |
| --- | --- | --- |
| `reference` | 30 passed | 参考实现满足教师验收和本次附加测试 |
| `broken` | 23 failed, 7 passed | 故障对照按预期被断言拒绝 |
| 实现前的 `student` | 30 failed | 三个函数尚未实现，抛出 `NotImplementedError` |
| 最终默认 `student` | **30 passed** | 三道基础题和本次附加测试全部通过 |

一次失败与修正：故障版本对 `[1, 2, 2, -1]` 返回了 `-1`，但原列表仍为 `[1, 2, 2, -1]`，未满足“原地删除末项”的承诺。正式实现先处理空列表，再调用 `items.pop()`；返回值与原列表变化均由测试核对。

读一段实现：`positive_squares` 每轮取出一个值；仅当它大于零时，将平方放入新列表。因此两次出现的 `3` 都保留为 `9`，零和负数被排除，原输入保持不变。

## 本人复跑

在 VS Code 的 WSL Terminal 中进入本仓库的 `week-05/`，执行：

```bash
uv run --locked pytest -q
```

打开 `practice.ipynb` 时选择 **W5 Python 3.12** kernel，再核对一处预测、实际输出以及原对象是否改变。远端结果在个人仓库的 **Actions → W5 data operations → W5 acceptance → Run student acceptance tests** 查看，需对应自己的提交编号。
