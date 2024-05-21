#Write a python program to Delete a file

import os
file_path = 'example.txt'
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"The file {file_path} has been deleted successfully.")
else:
    print(f"The file {file_path} does not exist.")
