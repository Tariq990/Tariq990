# Tariq Ziad

**Software Engineer · AI Agent Reliability · Developer Infrastructure · Automation**

I build systems that **verify what software and AI agents actually did**, instead of treating a successful response or command exit as proof. My work focuses on explicit trust boundaries, deterministic testing, safe tool execution, reliable recovery, and observable production behavior.

Founder of [RecepioHQ](https://github.com/RecepioHQ).

**Live, no-signup browser demo:** [Try Outbound OS's AI send-policy engine](https://recepiohq.github.io/outbound-os/) — change synthetic safety conditions and see exactly which checks return PASS, HOLD, or BLOCK. Runs in the browser with **no actual messages sent**.

**Official MCP Registry:** [Outbound OS — active, v0.2.1](https://registry.modelcontextprotocol.io/v0.1/servers?search=outbound-os), packaged as a public local-use OCI container at `ghcr.io/recepiohq/outbound-os-mcp:0.2.1` (verified in the [read-only GitHub Actions check](https://github.com/RecepioHQ/outbound-os/actions/runs/40092801181)). This is **not** a hosted public MCP endpoint or evidence of third-party adoption.

## Start here

| Project | What it solves | Availability |
| --- | --- | --- |
| **[Outbound OS](https://github.com/RecepioHQ/outbound-os)** | Evidence-gated outbound workflows: verify buyer fit, message claims, authorization, and delivery state before sending | **Open source — MIT** |
| **[Deep Seek Fix](https://github.com/Tariq990/deep-seek-fix)** | Checks coding-agent outcomes against task contracts, execution evidence, and deterministic verification gates | Source-available; non-commercial license |
| **[Unified MCP Control Plane](https://github.com/Tariq990/unified-mcp-control-plane)** | MCP tool discovery with OAuth 2.1, policy-based execution, server-side authorization and redaction | Source-available; non-commercial license |
| **[Windows Maintenance Orchestrator](https://github.com/Tariq990/windows-maintenance-orchestrator)** | Policy-driven update plans, bounded recovery, reboot-safe state, and verification of real machine outcomes | Source-available; non-commercial license |

**Try [Outbound OS v0.2.1](https://github.com/RecepioHQ/outbound-os/releases/tag/v0.2.1) in one command, without installing globally:**

```bash
npm exec --yes --package=https://github.com/RecepioHQ/outbound-os/releases/download/v0.2.1/outbound-os-0.2.1.tgz -- outbound-os demo --compare
```

Requires Node.js 22+. The command was tested on Windows: it demonstrates both a permitted simulated action and a blocked, unverified mailbox with **zero real emails sent**. It downloads the package from GitHub, not the npm registry. No Node.js? [Try the interactive browser demo](https://recepiohq.github.io/outbound-os/).

**Explore agent verification without live model keys:** [Deep Seek Fix first-run guide](https://github.com/Tariq990/deep-seek-fix/blob/main/docs/quickstart.md).

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
