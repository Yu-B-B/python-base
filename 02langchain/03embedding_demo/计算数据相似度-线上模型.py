import ast

import numpy as np
import pandas as pd
from langchain_huggingface import HuggingFaceEmbeddings

from my_llm import qwen37_embedding



model_name = "BAAI/bge-small-zh-v1.5"
model_kwargs = {'device': 'cuda'}  # 指定device可以有： cpu/cuda
encode_kwargs = {'normalize_embeddings': True}  # set True to compute cosine similarity

model = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs,
)


def context_2_embedding(text):
    resp = qwen37_embedding.embeddings.create(
        model='qwen3.7-text-embedding',  # 这里要使用向量模型
        dimensions=512,
        input=[text],
    )
    return resp.data[0].embedding
    # resp = model.embed_documents([text])
    # return resp[0]


def read_file(sourceFilePath, outputFilePath):
    file_context = pd.read_csv(sourceFilePath, index_col=0)

    spec_col_context = file_context[['Time', 'ProductId', 'UserId', 'Score', 'Summary', 'Text']]

    # 清洗 / 合并数据
    # 清洗数据，清除空行数据
    spec_col_context = spec_col_context.dropna()
    # 合并指列数据为新列
    spec_col_context[
        'summary_context'] = 'Summary:' + spec_col_context.Summary.str.strip() + '; Text' + spec_col_context.Text.str.strip()

    # 合并后的护具向量化
    spec_col_context['embedding'] = spec_col_context.summary_context.apply(lambda x: context_2_embedding(x))
    spec_col_context.to_csv(outputFilePath)


def calculate_cosine(a, b):
    """
    :param a: 向量a
    :param b: 向量b
    :return: 通过cosine计算两个向量相似度
    """
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# 从文件中读取出来的向量数据是字符串，首先需要将计算好的向量转为内存向量
def search_text(input, embedding_file, top=3):
    """

    :param input:  用户输入问题
    :param embedding_file:  存有向量数据的文件
    :param top: 前n条数据
    :return:
    """
    df_data = pd.read_csv(embedding_file)

    # 将存储的向量内容转为内存向量，这里是申明新的字段用来存储向量数据
    df_data['embedding_vector'] = df_data['embedding'].apply(ast.literal_eval)

    # 将输入内容转为向量
    input_vector = context_2_embedding(input)

    # 计算文件中向量与用户问题之间的相似度
    df_data['similarity'] = df_data.embedding_vector.apply(lambda x: calculate_cosine(x, input_vector))

    res = (
        df_data.sort_values('similarity', ascending=False).head(top)
        .summary_context.str.strip()
        # .Summary.str.strip()
        # .Text.str.strip()
    )

    for i in res:
        print(i)
        print('-'*30)


if __name__ == '__main__':
    read_file('../../fine_food_reviews_1k.csv', '../../train.csv')
    # search_text('delicious','train.csv')