
import sys
import re

# check all lines on STDIN
for line in sys.stdin:
    if re.search("restart", line):
        print("\nSystem started again: ", line)
    if re.search("exiting on signal", line):
        print("\nServer crashed: ", line)
        print("\nSystem crash detected: ", line)

