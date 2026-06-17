import chromadb

client = chromadb.PersistentClient(
    path="../vector_db/chroma"
)

collection = client.get_or_create_collection(
    name="review_memory"
)

def save_review(review, sentiment):

    collection.add(
        documents=[review],
        metadatas=[
            {"sentiment": sentiment}
        ],
        ids=[str(hash(review))]
    )

def search_review(text):

    result = collection.query(
        query_texts=[text],
        n_results=3
    )

    return result