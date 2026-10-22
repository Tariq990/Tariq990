# n8n Failed Execution & Webhook Debugging Checklist

*A practical diagnostic guide for broken n8n automations. This is a general methodology, not a claim about a particular client's workflow or a guaranteed fix.*

**First principle:** do not rebuild a workflow until you can reproduce the failure and identify the boundary where expected data stops matching actual data.

## 1. Establish an observable failure

Record the following **without copying secrets or real customer data**:

| Field | Example (synthetic) |
| --- | --- |
| Expected result | Webhook creates one CRM lead |
| Actual result | HTTP Request node returns 401 |
| Workflow status | Failed execution in the Executions view |
| First failing node | `Create CRM Lead` |
| Input shape | `{ "email": "test@example.invalid" }` |
| Downstream impact | No lead record created |

Find a failed execution in the workflow or project **Executions** view. Inspect the earliest meaningful failure instead of assuming the last node is the cause. Confirm whether execution data is available under the instance's retention settings.

## 2. If the webhook did not trigger

1. Confirm whether the external service called the correct URL, method, and path.
2. Distinguish **test** webhook URLs from **production** URLs. A working test request does not prove the production endpoint is configured.
3. Verify the workflow is published/active as required by your n8n version, and that the external service uses the intended endpoint.
4. If using a reverse proxy or self-hosting, check the public webhook base URL and HTTPS routing.
5. If the request arrived, inspect the received headers, content type, JSON structure, and any authentication requirement.

Do not disable authentication to make the webhook appear to work.

## 3. If an HTTP Request node failed

Check the **actual status code, sanitized response body, and outbound request format**.

| Result | First things to investigate |
| --- | --- |
| 400 / 422 | Required fields, types, encoding, endpoint contract |
| 401 | Missing or expired authentication; token type; header format |
| 403 | Authenticated identity lacks scope, permissions, or access |
| 404 | URL, route, resource ID, method, or environment |
| 409 | Duplicate state or concurrent update; inspect idempotency |
| 429 | Rate limits, provider quotas, backoff rules |
| 5xx | Provider outage, upstream failure, timeout/retry policy |

These status codes are diagnostic clues, not proofs of a specific root cause. Check the provider's API documentation before changing credentials or scopes.

## 4. Inspect mapping and expressions

- Compare the incoming item shape to the exact field path used by the failed node.
- Distinguish a missing field from an empty string, `null`, or an unexpected array.
- Check whether a previous node renamed a property, wrapped it in an object, or returned multiple items.
- Test a representative success input and at least one malformed/missing-field input.
- Keep the original workflow export as a reversible backup before changing production logic.

## 5. Protect against duplicate effects

**A successful retry can still create duplicate CRM records, notifications, invoices, or emails.** Before retrying a partially executed workflow:

- Determine which downstream actions already completed.
- Use an external event ID or stable idempotency key where supported.
- Check whether the target API provides upsert, deduplication, or idempotent-create semantics.
- Avoid blindly replaying a whole production execution when the first run may have already had side effects.

n8n supports retrying failed executions from the Executions view, but the operator remains responsible for understanding side effects.

## 6. Verify the fix instead of merely seeing a green check

A meaningful acceptance test should confirm:

1. The trigger receives the expected request.
2. Field validation produces the intended values.
3. The API reports success **and the downstream record actually exists**.
4. Error handling reports failures without hiding or duplicating effects.
5. A repeat event behaves according to the agreed deduplication policy.
6. The documented change is limited to the agreed scope.

**Handoff:** workflow export (when appropriate), list of nodes changed, representative sanitized test results, remaining limitations, and instructions for owner-controlled credentials.

## 7. What to share when requesting help

Safe to share: n8n version, deployment type, expected outcome, node names, sanitized error, synthetic request/response, and a workflow export with credentials and personal data removed.

**Never send passwords, live API keys, access tokens, cookies, credential exports, or customer records in chat.**

## Reference documentation

- [n8n: All executions and retrying failures](https://docs.n8n.io/workflows/executions/all-executions/)
- [n8n: Security audit](https://docs.n8n.io/hosting/securing/security-audit/)
- [n8n documentation](https://docs.n8n.io/)

---

### Need an existing n8n workflow repaired?

I work on scoped debugging of failed executions, webhook triggers, API authentication, and data mapping. Send a sanitized failure example and your expected result through the [n8n bug-fix service on Fiverr](https://www.fiverr.com/tariq97ziad/fix-your-n8n-workflow-webhook-api-and-ai-agent-errors).

This guide is educational and does not represent a delivered client project.
