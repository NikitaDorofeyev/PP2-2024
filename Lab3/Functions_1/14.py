from Functions import histogram

list = []

while True:
    num_input = input()
    if num_input == '':
        break

    num = int(num_input)

    list.append(num)

histogram(list)

