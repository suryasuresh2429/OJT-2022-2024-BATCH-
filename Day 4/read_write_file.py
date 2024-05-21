#Write a Python program to Read/Write to a File 

file_path = 'text.txt'
with open(file_path, 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is an example of writing to a file.\n")
    file.write("Python makes it easy!\n")

print(f"Data has been written to {file_path}")
