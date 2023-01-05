

import re

with open("log.txt", "r") as log:
    for l in log:
        if re.search("restart", l):
            # if "restart" is found in line, print whole line
            print(l)


import sys
import re

# check all lines on STDIN
for line in sys.stdin:
  # look for "restart"
  if re.search("restart", line):
    # i restart is found, print whole line
    print(line)
