def spy_game(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

listOfNum = []

while True:
    num_input = input()
    if num_input == '':
        break

    num = int(num_input)

    listOfNum.append(num)

result = spy_game(listOfNum)

if(result):
    print("True")
else:
    print("False")