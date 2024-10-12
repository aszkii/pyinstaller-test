
import sys
import subprocess

command = ['dist/main']
result = subprocess.run(command)
sys.exit(0)
