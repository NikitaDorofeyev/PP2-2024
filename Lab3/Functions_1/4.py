def filter_prime(numbers):
    prime_list = []
    for element in numbers:
        if element < 2:
            continue
        isPrime = True

        for i in range(2, int((element / 2) + 1)):
            if element % i == 0:
                isPrime = False
                break

        if isPrime:
            prime_list.append(element)
    
    return prime_list

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = filter_prime(num_list)

print(result)

