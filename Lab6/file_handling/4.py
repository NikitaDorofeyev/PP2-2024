def count_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            print("Number of lines in the file:", num_lines)
    except FileNotFoundError:
        print("File not found!")

file_name = input('Input a file name (.txt): ')

count_lines(file_name)
