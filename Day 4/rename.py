#Write a Python program that renames a file named ‘old_name.txt to’ ‘new_name.txt’.
import os
def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' has been renamed to '{new_name}' successfully.")
    except FileNotFoundError:
        print(f"File '{old_name}' not found.")
    except FileExistsError:
        print(f"A file named '{new_name}' already exists.")

old_name = "sample.txt"
new_name = "sample1.txt"
rename_file(old_name, new_name)
