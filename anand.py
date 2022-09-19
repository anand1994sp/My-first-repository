# Find factors

def fac(n):
    for i in range(2, n + 1):
        if n % i == 0:
            factors.append(i)
            i += 1
    print("Factors are :" + str(factors))
n = int(input("Enter a Number: "))
factors = []
fac(n)

