"""Safe maintenance placeholder for the legacy Pandora repository.

The previous setup.py executed a long list of shell commands, including
system package-manager operations, at import/run time. That behavior is
unsafe and is intentionally not reproduced here.

This repository's legacy entry point advertises offensive capabilities and
has not been audited for safe execution. Do not use this file to install
packages or launch the application. For defensive work, create an isolated
virtual environment and review dependencies and source code manually first.
"""

def main() -> int:
    print(
        "Automatic installation is disabled: the legacy Pandora codebase "
        "requires a security review before it can be run."
    )
    print(
        "No commands were executed and no packages were installed. "
        "See SECURITY.md for safe-use guidance."
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
