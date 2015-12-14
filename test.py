import os
import subprocess
import sys

print("running test.py")
print("sys.executable", sys.executable)

second = os.path.join('.', 'second.py')
print("trying to launch", second, "through the shell")
subprocess.call(second, shell=True)

print("doing it again and capturing output")
out = subprocess.check_output(second, shell=True).decode()
print("here's the output:", repr(out))
assert os.environ['PYTHON'] in out, "look for the PYTHON path in there"
