# Supabase Auth Redirect Diagnostics — Offline Checker

A dependency-free Node.js command-line helper for Lovable, Bolt and Replit app developers investigating Supabase Auth URL configuration problems.

**Safety:** no network requests; no passwords, API keys, tokens or real account data needed. It only compares static URLs. It does not emulate Supabase Auth or verify OAuth, sessions, wildcard patterns, Row Level Security or production security.

## Running the diagnostic

1. Download check.cjs and example-config.json.
2. Replace the synthetic example siteUrl, redirectTo and redirectAllowList with sanitized configuration values.
3. Run `node check.cjs example-config.json`.
4. Run local tests with `node test.cjs`.

Checks missing/malformed URLs, non-HTTPS production settings, and exact URL equality against the site URL or explicit allowlist entries. Wildcards are **not** evaluated; the tool deliberately asks you to verify them in Supabase. Exact equality here does **not** guarantee that a redirect succeeds.

## Debugging checklist

1. Check Site URL and Redirect URLs in Supabase Auth URL Configuration. `redirectTo` should match the configured allowed redirect URLs.
2. Distinguish the application's post-login redirectTo from the provider's separate OAuth callback/redirect settings.
3. Inspect browser network and auth session persistence on the callback route.
4. If login succeeds but data cannot be accessed, investigate database grants and RLS as a separate concern. Never disable RLS as an ad hoc fix.
5. Reproduce and retest with safe, synthetic accounts and sanitized logs.

Official references: [Supabase Auth redirect URL guide](https://supabase.com/docs/guides/auth/redirect-urls) and [Supabase RLS guide](https://supabase.com/docs/guides/database/postgres/row-level-security).

Need help with a real app? [Lovable/Bolt/Replit/Supabase debugging service on Fiverr](https://www.fiverr.com/tariq97ziad/fix-bugs-in-your-lovable-bolt-replit-or-supabase-app).

Educational diagnostic only, not evidence of completed client work.