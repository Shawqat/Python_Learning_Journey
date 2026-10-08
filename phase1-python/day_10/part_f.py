# detect environment
import sys
in_venv = sys.prefix != sys.base_prefix
print(f"Python version: {sys.version.split()[0]}")
print(f"Interpreter: {sys.executable}")
print(f"Inside a venv: {in_venv}")

try:
    import requests
    print("requests installed: True")
except ImportError:
    print("there's an error while trying get requests mostly uninstalled")


