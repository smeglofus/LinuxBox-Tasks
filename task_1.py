
import sys
import re

# check all lines on STDIN
for line in sys.stdin:
    # if restart in line, print whole line
    if re.search("restart", line):
        print("\nSystem started again: ", line)
    # if server crashed on signal, print whole line with warning that system crash is detected
    if re.search("exiting on signal", line):
        print("\nSystem crash detected: ", line)

