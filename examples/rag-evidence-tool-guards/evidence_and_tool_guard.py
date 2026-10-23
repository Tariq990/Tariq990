"""Offline evidence/citation + tool-authorisation demonstration.

This is a small control-layer example, NOT a complete RAG pipeline.
There are no embeddings, PostgreSQL, LLM calls, or external API calls.
"""
from __future__ import annotations
from dataclasses import dataclass
import re
from typing import Any

@dataclass(frozen=True)
class Evidence:
    document_id: str
    chunk_id: str
    text: str
    relevance: float

def select_evidence(chunks: list[Evidence], threshold: float = 0.65, limit: int = 3) -> list[Evidence]:
    """Return unique, source-addressable candidates above a threshold."""
    seen: set[tuple[str, str]] = set()
    output: list[Evidence] = []
    for item in sorted(chunks, key=lambda x: x.relevance, reverse=True):
        if item.relevance < threshold or not item.text.strip():
            continue
        if not re.fullmatch(r"[A-Za-z0-9_.-]{1,64}", item.document_id):
            continue
        if not re.fullmatch(r"[A-Za-z0-9_.-]{1,64}", item.chunk_id):
            continue
        key = (item.document_id, item.chunk_id)
        if key in seen:
            continue
        seen.add(key)
        output.append(item)
        if len(output) >= limit:
            break
    return output

def evidence_preview(chunks: list[Evidence]) -> dict[str, Any]:
    """Show supported excerpts or abstain; never generate unverified claims."""
    accepted = select_evidence(chunks)
    if not accepted:
        return {"status": "insufficient_evidence", "answer": None, "citations": []}
    return {
        "status": "evidence_available",
        "answer": None,  # Deliberately no LLM generation in this demo
        "citations": [{"source": x.document_id, "chunk": x.chunk_id, "excerpt": x.text[:150]} for x in accepted],
    }

ALLOWED_ACTIONS = frozenset({"lookup_order_status"})

class DeniedToolCall(ValueError):
    pass

def authorize_tool(name: str, args: dict[str, Any], permissions: set[str]) -> dict[str, str]:
    """Pure validation. Actual tool calls must occur in a separate privileged process."""
    if name not in ALLOWED_ACTIONS or name not in permissions:
        raise DeniedToolCall("Tool not allowed")
    if set(args) != {"order_id"}:
        raise DeniedToolCall("Unexpected tool arguments")
    identifier = args["order_id"]
    if not isinstance(identifier, str) or not re.fullmatch(r"ORD-[A-Z0-9]{4,12}", identifier):
        raise DeniedToolCall("Invalid identifier")
    return {"authorized_action": name, "order_id": identifier, "executed": "false"}

if __name__ == "__main__":
    items = [Evidence("guide-v1", "section-3", "Approved excerpt from an example document.", 0.92)]
    print(evidence_preview(items))