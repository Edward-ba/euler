# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

if __name__ == '__main__':
    total, sieve = 0, [True] * 2000000
    for i in range(2, 2000000):
        if sieve[i]:
            total += i
            for j in range(i * i, 2000000, i):
                sieve[j] = False
    print(total)
