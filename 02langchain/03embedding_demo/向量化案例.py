
from openai import OpenAI

from env_util import ALI_BASE_URL, ALI_API_KEY
client = OpenAI(
    api_key=ALI_API_KEY,
    base_url=ALI_BASE_URL,
)

text = 'I like llm.'
resp = client.embeddings.create(
    model='qwen3.7-text-embedding', # 这里要使用向量模型
    dimensions=512, # 将数据转为512个向量
    input = text
)

print(resp.data[0].embedding)