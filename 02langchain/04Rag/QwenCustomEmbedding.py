from langchain_core.embeddings import Embeddings
from sentence_transformers import SentenceTransformer


class QwenCustomEmbedding(Embeddings):
    """
    定义一个千文3的Embedding和langchain整合类
    """

    def __init__(self, model_name):
        self.qwen3_embedding = SentenceTransformer(model_name)

    # 对文本内容做向量化
    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self.qwen3_embedding.encode(texts)

    # 对用户输入内容做向量化
    def embed_query(self, text: str) -> list[float]:
        return self.embed_documents([text])[0]
