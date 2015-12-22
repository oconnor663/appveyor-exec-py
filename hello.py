#! /usr/bin/env python3

import sys

# We deliberately use Python-3-only print flags, to make sure we're running
# under Python 3.
print("OH MY GOSH ITS WORKING", sys.version, file=sys.stderr)
