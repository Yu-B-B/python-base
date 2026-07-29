from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B",
                            # model_kwargs={"attn_implementation": "flash_attention_2", "device_map": "auto"},
                            )

resp = model.encode([
    'I like llm.',
    '成都今天好热哦'
])

print(resp[0])
print(len(resp[0]))
