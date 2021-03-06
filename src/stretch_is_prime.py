import time
import math
# Base Case


def is_prime(num):
    if (num <= 3):
        return num >= 1
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# OPTIMIZATIONS

# 1. Capping the max number to be tested at √n (if a number is not prime, one of the factors has to be less than or equal to it's squareroot)

def is_prime_1(num):
    sqrt = math.floor(math.sqrt(num))
    if (num <= 1):
        return num >= 1
    for i in range(2, sqrt + 1):
        if num % i == 0:
            return False
    return True

# 2. 6K + 1 Optimization (all prime numbers > 6 can be expressed as 6k +/- 1)


def is_prime_2(n):
    i = 5
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False

    while n > i**2:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


# Test
# start = time.time()

# for i in range(100000):
#     x = is_prime(i)

# stop = time.time()
# print(stop-start)


# Sieve of Eratosthenes


def daSieve(n):
    p = 2
    prime = [True for i in range(n + 1)]

    for i in range(p, math.floor(math.sqrt(n))):
        if prime[i]:
            for j in range(i**2, n + 1, i):
                prime[j] = False

    for i in range(n + 1):
        if prime[i]:
            print(i, end=(", "))


daSieve(40)
