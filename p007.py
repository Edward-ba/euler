# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
import math

if __name__ == '__main__':
    prime = []
    check = 2
    while len(prime) < 10001:
        for i in range(2, int(math.sqrt(check))+1):
            if check % i == 0:
                break
        else:
            prime.append(check)

        check += 1
    print(prime[10000])
