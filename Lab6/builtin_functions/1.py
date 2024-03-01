from functools import reduce

nums_list = []

while True:
    nums = input()
    if nums == '':
        break
    nums_list.append(int(nums))

result = str(reduce(lambda x, y : x * y, nums_list))

print(f"The result of the multiplication is {result}")

