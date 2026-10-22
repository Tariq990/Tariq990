# n8n Lead Intake — Safe Dry-Run Example

A self-contained **illustrative workflow** demonstrating input validation and per-execution deduplication before a CRM action. This is NOT a production CRM integration. It has no webhooks, credentials, outbound requests or real CRM writes. It runs from a manual trigger with synthetic records.

## Flow

Manual Trigger → Generate Synthetic Form Events → Validate and Deduplicate → Preview CRM Actions (No API Calls).

## Try it

1. Download [workflow.json](workflow.json).
2. In the n8n editor, choose Import from File and select it.
3. Run the workflow manually; inspect the Code node outputs.

| Event | Condition | Expected dry-run action |
| --- | --- | --- |
| evt_demo_001 | valid | SIMULATED_CRM_CREATE |
| evt_demo_002 | invalid email | SKIPPED |
| evt_demo_001 | duplicate within run | SKIPPED |
| evt_demo_003 | valid | SIMULATED_CRM_CREATE |

Local test: run "node test-demo.cjs". The script executes the exact Code node JavaScript using an input stub and verifies four cases. **The JSON has not yet been import-tested against a live n8n instance.**

## Production gaps to address

- Replace synthetic data with a secured, authenticated trigger.
- This in-memory Set only deduplicates within one execution and is **insufficient for production**. Use an atomic persistent idempotency mechanism for retries across executions.
- Add field contracts, rate limits, CRM-owned credentials, retry/timeout policy, privacy controls and recovery tests.
- Verify downstream effects rather than relying solely on successful execution status.

See [official n8n import documentation](https://docs.n8n.io/build/manage-workflows/export-and-import) and [Code node documentation](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/).

For a scoped real integration, [see the n8n automation service on Fiverr](https://www.fiverr.com/tariq97ziad/build-n8n-automation-workflows-with-apis-and-ai-agents).

Educational sample only; no client work or revenue claims.