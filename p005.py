# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

if __name__ == '__main__':
    found = False
    num = 0
    while not found:
        num += 1
        for i in range(11, 21):
            if num % i != 0:
                break
            if i == 20:
                found = True
    print(num)
# could also be done by multiplying the prime numbers under 20 then by 8 and 3 2*3*5*7*11*13*17*19*8*3
