
import sys
import subprocess

command = ['pyinstaller', '--onefile', 'src/pyinstaller_test/main.py']
result = subprocess.run(command)
sys.exit(result.returncode)

