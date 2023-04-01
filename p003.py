# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

if __name__ == '__main__':
    prime = []
    for i in range(2, 10000):
        for j in range(2, i+1):
            if j == i:
                prime.append(i)
                break
            if i % j == 0:
                break

    num = 600851475143
    largest_prime = 0
    while num > 1:
        for i in prime:
            if num % i == 0:
                num /= i
                if largest_prime < i:
                    largest_prime = i
                break
    print(largest_prime)
