def write_list_to_file(file, list):
    with open(file, 'w') as file:
        for el in list:
            file.write(str(el) + '\n')
    print(f"List has been written to {file_name} succesfully")


file_name = 'Result.txt'

list = ["guitar, drums, bass, violin, piano"]

write_list_to_file(file_name, list)