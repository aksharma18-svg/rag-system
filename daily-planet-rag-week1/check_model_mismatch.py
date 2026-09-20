import numpy as np
from rag.embed import embed_query
small = embed_query("how is the new arena being paid for?", model="text-embedding-3-small")
large = embed_query("how is the new arena being paid for?", model="text-embedding-3-large")

print("Vector small length:", len(small))
print("Vector large length:", len(large))
print(np.dot(small, large))