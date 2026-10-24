# Tariq Ziad

**Software Engineer · AI Agent Reliability · Developer Infrastructure · Automation**

I build systems that **verify what software and AI agents actually did**, instead of treating a successful response or command exit as proof. My work focuses on explicit trust boundaries, deterministic testing, safe tool execution, reliable recovery, and observable production behavior.

Founder of [RecepioHQ](https://github.com/RecepioHQ).

## Start here

| Project | What it solves | Availability |
| --- | --- | --- |
| **[Outbound OS](https://github.com/RecepioHQ/outbound-os)** | Evidence-gated outbound workflows: verify buyer fit, message claims, authorization, and delivery state before sending | **Open source — MIT** |
| **[Deep Seek Fix](https://github.com/Tariq990/deep-seek-fix)** | Checks coding-agent outcomes against task contracts, execution evidence, and deterministic verification gates | Source-available; non-commercial license |
| **[Unified MCP Control Plane](https://github.com/Tariq990/unified-mcp-control-plane)** | MCP tool discovery with OAuth 2.1, policy-based execution, server-side authorization and redaction | Source-available; non-commercial license |
| **[Windows Maintenance Orchestrator](https://github.com/Tariq990/windows-maintenance-orchestrator)** | Policy-driven update plans, bounded recovery, reboot-safe state, and verification of real machine outcomes | Source-available; non-commercial license |

**Install the MIT-licensed [Outbound OS v0.2.1](https://github.com/RecepioHQ/outbound-os/releases/tag/v0.2.1) directly from a verified GitHub Release:**

```bash
npm install --global https://github.com/RecepioHQ/outbound-os/releases/download/v0.2.1/outbound-os-0.2.1.tgz
outbound-os demo --compare
```

Requires Node.js 22+. The installation and demo were verified on Windows; the demo uses synthetic data and does **not** send live emails. This release asset is **not an npm-registry publication**. See the [Outbound OS README](https://github.com/RecepioHQ/outbound-os#readme) for the safety model and full source-install option.

**Explore agent verification without live model keys:** [Deep Seek Fix first-run guide](https://github.com/Tariq990/deep-seek-fix/blob/main/docs/quickstart.md) (available on `main` after its [documentation PR](https://github.com/Tariq990/deep-seek-fix/pull/19) is merged).

## Other engineering systems

- **[Social Radar Platform](https://github.com/Tariq990/social-radar-platform)** — React/Express/PostgreSQL and Capacitor Android architecture, tenant isolation, AI rule evaluation, and security-focused device ingestion. Alpha; physical-device launch gates remain open.
- **[MT5 AI Trading Runtime](https://github.com/Tariq990/mt5-ai-trading-runtime)** — Demo-only Python/FastAPI execution architecture with broker adapters, deterministic risk controls, persistence, and failure reconciliation. Real-money execution is hard-blocked.

## Engineering approach

`Python` · `TypeScript` · `FastAPI` · `React` · `PostgreSQL` · `SQLite` · `MCP` · `OAuth` · `CI` · `AI Agents` · `Test Automation`

1. **Observe** the failure and gather reproducible evidence.
2. **Constrain** unsafe or uncertain side effects behind explicit policy.
3. **Fix** the smallest verified root cause.
4. **Test** deterministic acceptance and failure paths.
5. **Report** verified, failed, blocked, and untested outcomes separately.

I don't claim adoption, benchmark superiority, or a passing CI result without evidence.

## Engineering notes and examples

- [n8n debugging checklist](docs/n8n-debugging-checklist.md)
- [n8n lead-intake dry-run workflow](examples/n8n-lead-intake/README.md) — synthetic, no live sends
- [Supabase Auth redirect URL checker](examples/supabase-auth-redirect-check/README.md)
- [RAG evidence and restricted tool-call guards](examples/rag-evidence-tool-guards/README.md)

## Collaboration

I work on application debugging, integrations, backend systems, agent infrastructure, and reliable automation. Open a well-scoped [GitHub issue for Outbound OS](https://github.com/RecepioHQ/outbound-os/issues) for project-related bugs or contributions, and consult each repository's licensing and security policy first.

For commercial engagements:

- [AI-generated app and Supabase debugging](https://www.fiverr.com/tariq97ziad/fix-bugs-in-your-lovable-bolt-replit-or-supabase-app)
- [n8n webhook, API, and agent debugging](https://www.fiverr.com/tariq97ziad/fix-your-n8n-workflow-webhook-api-and-ai-agent-errors)
- [n8n automation and integrations](https://www.fiverr.com/tariq97ziad/build-n8n-automation-workflows-with-apis-and-ai-agents)
- [LinkedIn](https://www.linkedin.com/in/tariq--ziad/)
