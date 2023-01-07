
import os
import sys
import fnmatch

#define function, which takes 2 arguments. Directory and file name
def find_files(directory, file_name):
# Loop through all files and directories in directory and print found files with whole path
  for root, dirs, files in os.walk(directory):
    for file in files:
      if fnmatch.fnmatch(file, file_name):
        print(os.path.join(root, file))

#script parameters
directory = sys.argv[1]
file_name = sys.argv[2]

#call function with arguments
find_files(directory, file_name)