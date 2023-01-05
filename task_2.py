

import os
# give directory path and name/mask of desired file
dir_path = "C:\\Users\\Dell\\Desktop"
file_name = "komba.txt"

# Loop throught all files and directiries in dir_path and print found files
for root, dirs, files in os.walk(dir_path):
  for file in files:
    if file == file_name:
      print(os.path.join(root, file))
