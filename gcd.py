def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("GCD of 24 and 36 is", gcd(24, 36))
