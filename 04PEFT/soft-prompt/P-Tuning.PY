'''
也是在输入的embdding之前添加一些 embdding

prompt tunning 是将输入内容转为参数后初始化，通过正向传播、反向传播调整参数
p tunning 是将输入内容前添加额外层（层中有参数，参数更多，多的参数为“多层全连接MLP” 或 LSTM 中的参数）

p-tunnint 脚本与 prompt tunning 代码结构差不多

'''