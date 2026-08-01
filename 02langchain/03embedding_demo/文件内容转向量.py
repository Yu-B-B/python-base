import pandas as pd
from langchain_huggingface import HuggingFaceEmbeddings

model_name = "BAAI/bge-small-zh-v1.5"
model_kwargs = {'device': 'cuda'} # 指定device可以有： cpu/cuda
encode_kwargs = {'normalize_embeddings': True} # set True to compute cosine similarity


model = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs,
)



def context_2_embedding(text):
    resp = model.embed_documents([text])
    return resp[0]

def read_file(sourceFilePath, outputFilePath):
    file_context = pd.read_csv(sourceFilePath, index_col=0)

    spec_col_context = file_context[['Time','ProductId','UserId','Score','Summary','Text']]

    # 清洗 / 合并数据
    # 清洗数据，清除空行数据
    spec_col_context = spec_col_context.dropna()
    # 合并指列数据为新列
    spec_col_context['summary_context'] = 'Summary:'+spec_col_context.Summary.str.strip() + '; Text'+spec_col_context.Text.str.strip()

    # 合并后的护具向量化
    spec_col_context['embedding'] = spec_col_context.summary_context.apply(lambda x:context_2_embedding(x))
    spec_col_context.to_csv(outputFilePath)

if __name__ == '__main__':
    read_file('../../fine_food_reviews_1k.csv', 'train.csv')