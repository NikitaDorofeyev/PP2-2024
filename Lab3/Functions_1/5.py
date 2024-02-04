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

userString = input()
result = permutations(userString)

for i in result:
    print(i)