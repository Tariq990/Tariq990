# Evidence citations and restricted tool-calls — Python demo

A **standalone offline demonstration** of two guardrails relevant to a document-question-answering/RAG application:

1. Only pass source-addressable, scored chunks above a minimum threshold; abstain when no evidence is available. Show document and chunk IDs alongside the actual excerpts.
2. Validate tool name, explicit caller permissions, exact argument schema, and identifiers before a privileged service executes a tool.

Run tests without installing dependencies:

```bash
python -m unittest -v test_evidence_and_tool_guard.py
```

This is **not** a complete RAG system. The ranking scores are provided as inputs; it includes no real embeddings, vector database, parser, LLM, FastAPI server, prompt-injection defence, or network integration. `authorize_tool` returns validation metadata and deliberately does not execute anything. A real build must add those components and enforce tool permissions server-side, independently of model output.

Example output: `status: evidence_available`, `answer: null`, and source-level citations for suitable excerpts; or `status: insufficient_evidence` with no fabricated answer.

Source code and ten unit tests are provided for review; this is independent engineering evidence, **not previous paid client work**.

For larger Python, API, retrieval, and testing projects, see the [engineering profile](https://github.com/Tariq990).