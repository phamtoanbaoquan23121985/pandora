# Security Policy

## Scope and authorization

Use this repository only for defensive security learning and testing systems you own or are explicitly authorized to assess. Define written scope, permitted methods, time windows, and stop conditions before any test.

This project has historically advertised capabilities associated with denial of service, exploitation, credential or database access, surveillance, doxxing, and malware. Those capabilities can cause real harm. This maintenance branch does not add to, repair, or operationalize those features. Do not run the legacy entry point against third-party systems.

## Safe handling

- Run experiments in an isolated, disposable lab with no route to production networks.
- Never enter real credentials, personal data, API keys, or customer data into test fixtures.
- Do not run scripts as root/Administrator unless a separately reviewed, narrowly scoped requirement makes it essential.
- Review every script before execution. Treat downloaded code and dependency install scripts as untrusted.
- Pin and audit dependencies; install into a virtual environment rather than the system Python.
- Stop immediately if a test affects systems outside the approved scope.

## Reporting

Do not publish exploit details, personal data, secrets, or weaponized proof-of-concept code in an issue. For a vulnerability affecting a third party, use that party's coordinated disclosure process.

## Maintenance goals

Future work should prioritize safe defaults, dependency hygiene, deterministic tests, clear authorization boundaries, and defensive-only functionality (for example, local configuration checks and passive analysis of user-supplied artifacts).