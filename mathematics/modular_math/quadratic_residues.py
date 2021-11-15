p = 29
ints = [14, 6, 11]

answers = [x for x in range(1, p, 1) if (x**2 % p) in ints]
answer = min(answers)
print(answer)

# flag: 8