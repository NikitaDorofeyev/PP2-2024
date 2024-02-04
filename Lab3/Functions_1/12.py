def histogram(numbers):
    for el in numbers:
        while el > 0:
            print('* ', end='')
            el -= 1
        print()
    

list = []

while True:
    num_input = input()
    if num_input == '':
        break

    num = int(num_input)

    list.append(num)

histogram(list)