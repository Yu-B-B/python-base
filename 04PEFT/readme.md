# PERT模型微调

## 理论
### 微调 & RAG

微调（SFT）：在基础的模型上增加其他参数，使模型更聪明。

RAG：

### 指令数据集构造方式

## BitFit

选择模型中参数一部分进行多次调整训练，其他参数冻结起来


## prompt-tuning

基于外部模型，将自定义数据经过训练后拼接到输入层input embdding前。

同一个任务训练出来的Virtual Token是相同的。

全量微调 ：
- 更新 Virtual Token 与 Input embedding 中所有参数

Prompt Tuning：
- update only prompt weights bases on loss（只更新Virtual Tokens）
- 输入层中的权重与向量全被锁住，并锁定基模型
- 从结果上看 loss 越小越好，且比hard prompt更优

模型处理多任务输入：
- 不同任务的Virtual Token 跟随此次输入的内容而改变


prompt tuning 在参数量达到一定数量时，能媲美全量调参；但若参数量不足时，评估指标上达不到预期值

