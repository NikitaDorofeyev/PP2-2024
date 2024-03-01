import os

def delete_file(file_path):
    if not os.path.exists(file_path):
        print("File doesn't exist.")
        return
    
    if not os.access(file_path, os.W_OK):
        print("Permission denied: You do not have write access to this file.")
        return

    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except OSError as e:
        print(f"Error: {e.strerror}")


file_path = input("Enter the file path to delete: ")
delete_file(file_path)
