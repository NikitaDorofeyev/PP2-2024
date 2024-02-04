import math

def histogram(numbers):
    for el in numbers:
        while el > 0:
            print('* ', end='')
            el -= 1
        print()

def unique_elements(input_list):
    unique_list = []

    for el in input_list:
        if el not in unique_list:
            unique_list.append(el)

    return unique_list 

def spy_game(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def permutations(s):
    if len(s) == 1:
        return [s]
    
    result = []

    for el in range(len(s)):
        current_char = s[el]
        remaining_chars = s[:el] + s[el+1:]
        remaining_permutations = permutations(remaining_chars)

        for permutation in remaining_permutations:
            result.append(current_char + permutation)

    return result

def solve_puzzle(numheads, numlegs):
    chicken_legs = numheads * 2
    rabbit_legs = numlegs - chicken_legs
    rabbits = int(rabbit_legs / 2)
    chickens = int(numheads - rabbits)

    return (rabbits, chickens)

def solve_puzzle(numheads, numlegs):
    chicken_legs = numheads * 2
    rabbit_legs = numlegs - chicken_legs
    rabbits = int(rabbit_legs / 2)
    chickens = int(numheads - rabbits)

    return (rabbits, chickens)

def grams_to_ounces_converter(grams):
    ounces = grams / 28.3495231
    return ounces

def volumeOfSphere(radius):
    volume = 4/3 * math.pi * radius**3
    return volume

def palindrom(word):
    if word == word[::-1]:
        return True
    return False