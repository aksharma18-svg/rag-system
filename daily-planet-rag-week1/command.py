from rag.embed import embed_query;
v = embed_query("arena budget");
print(len(v));
print(v[:5]);