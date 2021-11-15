p = 29
ints = [14, 6, 11]

ans = [x for x in range(p) if (x**2 % p) in ints]
answer = min(ans)
print(answer)