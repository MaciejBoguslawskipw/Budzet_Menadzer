import sys
from cx_Freeze import setup, Executable

base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="Budzet Menago",
    version="1.0",
    description="Aplikacja Do zarzadzania budzetem",
    executables=[Executable("budgetmenago.py", base=base)],
)
