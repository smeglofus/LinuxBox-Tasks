
import os
import sys
import fnmatch

def find_files(directory, file_name):
  for root, dirs, files in os.walk(directory):
    for file in files:
      if fnmatch.fnmatch(file, file_name):
        print(os.path.join(root, file))

directory = sys.argv[1]
file_name = sys.argv[2]

find_files(directory, file_name)