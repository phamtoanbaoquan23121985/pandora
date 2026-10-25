# Pandora — Security Review Required

This repository contains legacy Python code that advertises a mixture of security-related features, including denial-of-service, exploitation, unauthorized data access, surveillance, doxxing, and malware creation. It has **not** been audited for safe execution.

## Status

- **Not production-ready.**
- **Do not run the legacy `pandora.py` entry point against public or third-party systems.**
- The former `setup.py` ran shell and system package-manager commands automatically. That installer has been disabled in this branch; it now exits without installing packages or executing system commands.
- No claim is made that the rest of the legacy code is safe.

## Safe contribution scope

This project should be improved as a defensive security learning and maintenance project. Appropriate work includes:

- Removing unsafe implicit command execution and dangerous defaults.
- Dependency inventory, vulnerability review, and reproducible isolated environments.
- Unit tests for pure functions and static safety checks.
- Passive analysis of user-provided files and local configuration.
- Clear documentation of authorization, scope, privacy, and data handling.
- Cross-platform compatibility and maintainability improvements that do not enable offensive capabilities.

This branch intentionally does not add, fix, or optimize DDoS, exploitation, credential theft, unauthorized scanning, surveillance, doxxing, or malware functionality.

## Safe handling

1. Review source files before executing anything.
2. Use an isolated disposable virtual machine with no production or third-party network access.
3. Never use real credentials, secrets, or personal/customer data in test fixtures.
4. Do not run legacy scripts with root/Administrator privileges.
5. Treat all dependencies and downloaded artifacts as untrusted until reviewed.

See [SECURITY.md](SECURITY.md) for the security policy and reporting guidance.

## Current verification limits

The installer change is a narrow safety measure, not a complete security audit. The legacy entry point and its dependencies have not been executed or validated. Any future release should require automated tests, dependency checks, and a documented review of the remaining entry points before it can be considered safe.
