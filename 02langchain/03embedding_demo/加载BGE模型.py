# from langchain_community.embeddings import HuggingFaceBgeEmbeddings
# 或者使用，上面内容将不在维护
from langchain_huggingface import HuggingFaceEmbeddings

model_name = "BAAI/bge-small-zh-v1.5"
model_kwargs = {'device': 'cuda'} # 指定device可以有： cpu/cuda
encode_kwargs = {'normalize_embeddings': True} # set True to compute cosine similarity

# 第一次运行将自动下载模型到huggingface的缓存目录中
# default目录：C:\Users\user\.cache\huggingface\hub\models--BAAI--bge-small-zh-v1.5\snapshots
# 指定下载目录（修改环境变量）：HF_HOME=special_local

model = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs,
)

resp = model.embed_documents([
    'I like llm.',
    '成都今天好热哦'
])

print(resp[0])
print(len(resp[0]))