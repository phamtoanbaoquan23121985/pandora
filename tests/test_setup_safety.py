"""Regression tests for safe, reproducible dependency installation."""
import ast
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class SetupSafetyTests(unittest.TestCase):
    def test_setup_script_does_not_execute_shell_commands(self):
        source = (ROOT / "setup.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        forbidden_calls = []
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            func = node.func
            if isinstance(func, ast.Attribute) and func.attr == "system":
                forbidden_calls.append("os.system")
            if isinstance(func, ast.Name) and func.id in {"system", "popen"}:
                forbidden_calls.append(func.id)
            if isinstance(func, ast.Attribute) and func.attr == "run":
                for keyword in node.keywords:
                    if keyword.arg == "shell" and isinstance(keyword.value, ast.Constant) and keyword.value.value is True:
                        forbidden_calls.append("subprocess.run(shell=True)")
        self.assertEqual(forbidden_calls, [], f"Unsafe shell execution found: {forbidden_calls}")

    def test_setup_uses_python_module_installer_and_pinned_requirements_file(self):
        source = (ROOT / "setup.py").read_text(encoding="utf-8")
        self.assertIn('"-m", "pip", "install"', source)
        self.assertIn('"requirements.txt"', source)
        self.assertIn("check=True", source)


if __name__ == "__main__":
    unittest.main()
