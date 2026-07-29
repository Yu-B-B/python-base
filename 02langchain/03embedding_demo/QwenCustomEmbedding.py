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
        return self.embed_documents(texts)

    # 对用户输入内容做向量化
    def embed_query(self, text: str) -> list[float]:
        return self.embed_documents([text])[0]


if __name__ == '__main__':
    model = QwenCustomEmbedding('Qwen/Qwen3-Embedding-0.6B')

    resp = model.embed_documents([
        'I like llm.',
        '成都今天好热哦'
    ])

    print(resp[0])
    print(len(resp[0]))
