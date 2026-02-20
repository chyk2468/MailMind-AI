"""
rag_engine.py — RAG (Retrieval-Augmented Generation) engine for MailMind AI.

Uses ChromaDB as a persistent local vector store and sentence-transformers
to embed emails so that semantically similar examples can be retrieved and
injected into the Gemini prompt for richer, context-aware replies.
"""

import os
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

# ── Constants ──────────────────────────────────────────────────────────────────
CHROMA_PATH = os.path.join(os.path.dirname(__file__), ".chroma_db")
COLLECTION_NAME = "email_knowledge_base"
EMBED_MODEL = "all-MiniLM-L6-v2"

# ── Singleton client & collection ─────────────────────────────────────────────
_client: chromadb.PersistentClient | None = None
_collection = None


def _get_collection():
    """Return (or lazily create) the ChromaDB collection."""
    global _client, _collection
    if _collection is None:
        embed_fn = SentenceTransformerEmbeddingFunction(model_name=EMBED_MODEL)
        _client = chromadb.PersistentClient(path=CHROMA_PATH)
        _collection = _client.get_or_create_collection(
            name=COLLECTION_NAME,
            embedding_function=embed_fn,
            metadata={"hnsw:space": "cosine"},
        )
    return _collection


# ── Public API ─────────────────────────────────────────────────────────────────

def get_kb_count() -> int:
    """Return total number of documents stored in the knowledge base."""
    return _get_collection().count()


def add_email(email_text: str, tone: str = "general", source: str = "user") -> str:
    """
    Add an email document to the knowledge base.

    Parameters
    ----------
    email_text : str  – raw email body
    tone       : str  – tone label (e.g. 'Formal', 'Friendly')
    source     : str  – 'seed' | 'user' | 'upload'

    Returns the generated document ID.
    """
    collection = _get_collection()
    # Stable ID based on content hash so duplicates are idempotent
    import hashlib
    doc_id = hashlib.md5(email_text.encode()).hexdigest()
    existing = collection.get(ids=[doc_id])
    if existing["ids"]:
        return doc_id  # already present – skip

    collection.add(
        documents=[email_text],
        metadatas=[{"tone": tone, "source": source}],
        ids=[doc_id],
    )
    return doc_id


def retrieve_similar(email_text: str, k: int = 3) -> list[dict]:
    """
    Retrieve the top-k most semantically similar emails from the KB.

    Returns a list of dicts with keys: 'document', 'tone', 'distance'
    """
    collection = _get_collection()
    if collection.count() == 0:
        return []

    k = min(k, collection.count())
    results = collection.query(
        query_texts=[email_text],
        n_results=k,
        include=["documents", "metadatas", "distances"],
    )

    output = []
    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        output.append(
            {
                "document": doc,
                "tone": meta.get("tone", "general"),
                "distance": round(dist, 4),
            }
        )
    return output


def build_rag_context(email_text: str, k: int = 3) -> str:
    """
    Build a formatted context string from retrieved similar emails to inject
    into the LLM prompt.
    """
    similar = retrieve_similar(email_text, k=k)
    if not similar:
        return ""

    lines = ["--- Similar Email Examples (for reference) ---"]
    for i, item in enumerate(similar, 1):
        lines.append(f"\n[Example {i} | Tone: {item['tone']}]")
        lines.append(item["document"].strip())
        lines.append("")
    lines.append("--- End of Examples ---")
    return "\n".join(lines)
