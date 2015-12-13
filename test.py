import os
import subprocess
import sys

print("running test.py")
print("sys.executable", sys.executable)

print("trying to launch second.py through the shell")
subprocess.call("second.py", shell=True)

print("doing it again and capturing output")
out = subprocess.check_output("second.py", shell=True)
print("here's the output:", repr(out))
assert os.environ['PYTHON'] in out, "look for the PYTHON path in there"
