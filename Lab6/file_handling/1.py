import os

def list_directories(path):
    directories = []

    for dir in os.listdir(path):
        dir_path = os.path.join(path, dir)
        if os.path.isdir(dir_path):
            directories.append(dir)
    return directories

def list_files(path):
    files = []

    for f in os.listdir(path):
        f_path = os.path.join(path, f)
        if os.path.isfile(f_path):
            files.append(f)
        return files
    
def list_all(path):
    all = os.listdir(path)
    return all

path = r'C:\KBTU\2 Semester\Programming Principles II\PP2-2024'

print("Directories:", list_directories(path))
print("Files:", list_files(path))
print("All Directories and Files:", list_all(path))
