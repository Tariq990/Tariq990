# Tariq Ziad

**Founder at [RecepioHQ](https://github.com/RecepioHQ) ([recepio.io](https://recepio.io)) · AI Agent Reliability · MCP Infrastructure · Deterministic Systems**

I architect systems that **verify what software and AI agents actually executed**—enforcing explicit trust boundaries, policy-gated tool execution, deterministic test gates, and observable recovery across production workflows.

---

## Live Interactive Proof

- **Official MCP Registry:** [Outbound OS (`v0.2.1`)](https://registry.modelcontextprotocol.io/v0.1/servers?search=outbound-os) — distributed as a local-use OCI container (`ghcr.io/recepiohq/outbound-os-mcp:0.2.1`) and verified in CI.
- **No-signup Browser Demo:** [Try the Outbound OS send-policy simulator](https://recepiohq.github.io/outbound-os/) — toggle safety conditions and inspect live `PASS`, `HOLD`, and `BLOCK` decisions in the browser with zero live sends.
- **One-command CLI Comparison (`Node.js 22+`):**

```bash
npm exec --yes --package=https://github.com/RecepioHQ/outbound-os/releases/download/v0.2.1/outbound-os-0.2.1.tgz -- outbound-os demo --compare
```

- **Local Agent Verification (no API keys required):** [Agent Reliability Plane quickstart](https://github.com/Tariq990/agent-reliability-plane/blob/main/docs/quickstart.md).

---

## Flagship Systems & Open Source

| Repository | What it solves | Stack | License |
| --- | --- | --- | --- |
| **[Outbound OS](https://github.com/RecepioHQ/outbound-os)** | Evidence-gated outbound automation: verifies buyer fit, message claims, authorization, and delivery state before sending | TypeScript · Node.js | MIT |
| **[Agent Reliability Plane](https://github.com/Tariq990/agent-reliability-plane)** | Deterministic verification control plane for coding agents with task contracts, loop guards, bounded evidence, and evals | Python · TypeScript | Source-available |
| **[Unified MCP Control Plane](https://github.com/Tariq990/unified-mcp-control-plane)** | Policy-gated MCP gateway with OAuth 2.1, provider adapters, risk classification, and credential redaction | TypeScript · Cloudflare Workers | Source-available |
| **[Production Governance Template](https://github.com/Tariq990/production-governance-template)** | Machine-first GitHub template enforcing contract-bound PR gates, policy baselines, and verified delivery | Python · GitHub Actions | MIT Template |
| **[Solana Program Integrity](https://github.com/Tariq990/solana-program-integrity)** | Read-only Rust/WASI plugin that SHA-256 fingerprints deployed on-chain BPF bytes before agents trust a protocol | Rust · WASI | MIT |
| **[Social Radar Platform](https://github.com/Tariq990/social-radar-platform)** | Multi-tenant social monitoring architecture with AI rule evaluation, tenant isolation, and Capacitor Android client | React · Express · PostgreSQL · Android | Source-available |

### Additional Engineering Systems

- **[Windows Maintenance Orchestrator](https://github.com/Tariq990/windows-maintenance-orchestrator)** (`PowerShell`) — Policy-driven workstation maintenance planner with provider isolation, reboot-safe state, bounded recovery, and regression tests.
- **[MT5 AI Trading Runtime](https://github.com/Tariq990/mt5-ai-trading-runtime)** (`Python · FastAPI`) — Demo-only execution runtime with broker adapters, deterministic risk gates, SQLite persistence, and watchdogs.

---

## Tech Stack & Engineering Principles

`Python` · `TypeScript` · `Rust` · `FastAPI` · `Node.js` · `React` · `PostgreSQL` · `Cloudflare Workers` · `MCP` · `OAuth 2.1` · `WASI` · `GitHub Actions`

1. **Observe** — Capture reproducible runtime evidence before proposing changes.
2. **Constrain** — Isolate risky side effects behind deterministic policy gates.
3. **Fix** — Resolve the minimal verified root cause at the trust boundary.
4. **Test** — Encode deterministic acceptance, rejection, and failure paths.
5. **Verify** — Treat bounded runtime artifacts—never LLM claims—as proof of completion.

---

## Engineering Notes & Reproducible Examples

- [n8n failed execution & webhook debugging checklist](docs/n8n-debugging-checklist.md)
- [RAG evidence citations & restricted tool-call guards (Python)](examples/rag-evidence-tool-guards/README.md)
- [Supabase Auth redirect URL diagnostics (Node.js)](examples/supabase-auth-redirect-check/README.md)
- [n8n lead-intake validation & deduplication dry-run](examples/n8n-lead-intake/README.md)

---

## Connect

- **[recepio.io](https://recepio.io)**
- **[RecepioHQ on GitHub](https://github.com/RecepioHQ)**
- **[LinkedIn — Tariq Ziad](https://www.linkedin.com/in/tariq--ziad/)**
