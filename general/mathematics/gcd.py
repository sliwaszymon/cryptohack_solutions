# i'm not using Euclid's Algorithm!!!
def gcd(a, b):
    a_divisors = []
    for x in range(1, a+1, 1):
        if a/x == a//x:
            a_divisors.append(x)
    b_divisors = []
    for x in range(1, b+1, 1):
        if b/x == b//x:
            b_divisors.append(x)
    # assuming that the numbers have the same divisor 
    # and it is a large number, iterating over the 
    # inverted list will be faster
    gcd = 1
    for x in a_divisors[::-1]:
        for y in b_divisors[::-1]:
            if x == y:
                gcd = x
                return gcd


a = 66528
b = 52920
print(gcd(a, b))
