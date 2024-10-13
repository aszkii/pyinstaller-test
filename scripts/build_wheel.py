
import sys
import subprocess

command = ['rye', 'build']
result = subprocess.run(command)
sys.exit(result.returncode)
