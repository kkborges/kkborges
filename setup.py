import cx_Freeze
import pywin

from cx_Freeze import setup, Executable
setup(
    name="K3FAgent-Install",
    version="1.0.0",
    options={"build_exe": {
             'packages': ["os", "sys", "ctypes", "win32con"],
             'include_msvcr': True,
            }},
            executables=[Executable("topProcessos.py", base="Win32GUI")]
    )