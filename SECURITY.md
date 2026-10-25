# Security Policy

## Scope and authorization

Pandora is a security-related codebase. Use it only on systems you own or where you have explicit, written authorization. Keep testing within the agreed scope, time window, and rate limits. Do not use it to disrupt services, gain unauthorized access, evade access controls, collect private information, deploy malware, or interfere with networks and devices.

## Safe development

- Prefer passive analysis and non-destructive checks by default.
- Use isolated local labs, intentionally vulnerable targets, and synthetic data for demonstrations.
- Require explicit target allowlists and conservative timeouts for any network-facing diagnostic feature.
- Never store credentials, session cookies, API keys, personal data, or target data in source control or logs.
- Do not run the project with elevated privileges unless a reviewed, narrowly scoped test genuinely requires it.
- Review every dependency and pin versions; do not run installation scripts that invoke arbitrary shell commands or system package managers.
- Record reproducible test steps and results. A successful syntax check is not evidence that network behavior is safe.

## Reporting a vulnerability

Do not publish exploitable details or other people's data in an issue. Contact the repository maintainer privately through a verified contact channel and include a concise reproduction, impact, affected revision, and a safe mitigation where possible.

## Current limitations

This policy is not a claim that every existing feature has been audited. Legacy functionality may be unsafe, unmaintained, or incompatible with current Python and dependency versions. Treat the code as untrusted until reviewed and tested in an isolated environment.
