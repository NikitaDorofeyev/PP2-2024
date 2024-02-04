def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

listOfNum = []

while True:
    num_input = input()
    if num_input == '':
        break

    num = int(num_input)

    listOfNum.append(num)

result = has_33(listOfNum)

if(result):
    print("True")
else:
    print("False")