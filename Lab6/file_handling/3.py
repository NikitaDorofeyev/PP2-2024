import os

specified_path = input('Please, Enter the path to check: ')

if not os.path.exists(specified_path):
    print("Path does not exist!")
else:
    print("The path content:")
    print(os.listdir(specified_path))