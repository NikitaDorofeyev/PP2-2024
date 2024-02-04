def unique_elements(input_list):
    unique_list = []

    for el in input_list:
        if el not in unique_list:
            unique_list.append(el)

    return unique_list 

input_list = [1, 2, 2, 3, 4, 4, 5]

result = unique_elements(input_list)

print(result)