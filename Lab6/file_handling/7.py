import os

source_path = r'C:\KBTU\2 Semester\Programming Principles II\PP2-2024\Lab6\file_handling\Source.txt'
destination_path = r'C:\KBTU\2 Semester\Programming Principles II\PP2-2024\Lab6\file_handling\Destination.txt'

with open(source_path, 'r') as source_file:
    contents = source_file.read()

with open(destination_path, 'w') as destination_file:
    destination_file.write(contents)


print("Content has been copied")