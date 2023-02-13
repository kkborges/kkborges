import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'Console'

executables = [
    Executable( 'Main.py', base=base, target_name='agentek3f' )
]

setup( name='agenK3F',
       version='1.0',
       description='Agente Monitoramento Projeto K3F',
       options={'build_exe': build_options},
       executables=executables )
