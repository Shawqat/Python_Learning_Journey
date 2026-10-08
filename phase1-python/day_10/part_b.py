# detect environment
import sys
in_venv = sys.prefix != sys.base_prefix
print(f"Inside a venv: {in_venv}")
print(f"Interpreter: {sys.executable}")
print(f"Python version: {sys.version.split()[0]}")

# output after i activate venv: 
# Inside a venv: True
# Interpreter: G:\Python-FCC\playwright-automation-journey\phase1-python\day_10\env\Scripts\python.exe
# Python version: 3.13.14