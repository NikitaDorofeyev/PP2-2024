def solve_puzzle(numheads, numlegs):
    chicken_legs = numheads * 2
    rabbit_legs = numlegs - chicken_legs
    rabbits = int(rabbit_legs / 2)
    chickens = int(numheads - rabbits)

    return (rabbits, chickens)


heads = 35
legs = 94

result = solve_puzzle(heads, legs)

rabbits, chickens = result # Unpack a tuple

print(f"The number of rabbits is {rabbits}\nThe number of chickens is {chickens}")