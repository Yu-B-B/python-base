from langchain_openai import OpenAIEmbeddings

from env_util import ALI_BASE_URL, ALI_API_KEY

embedding_model = OpenAIEmbeddings(
    api_key=ALI_API_KEY,
    base_url=ALI_BASE_URL,
    model="qwen3.7-text-embedding",
    dimensions=512
)

resp = embedding_model.embed_documents([
    'I like llm.'
])

print(f'第一条数据向量化后的数据结果{resp[0]}')
