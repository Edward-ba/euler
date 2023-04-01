# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.

if __name__ == '__main__':
    largest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i * j
            if largest > i*j:
                continue
            num = list(str(num))
            for k in range(5):
                if num[k] != num[k*-1 - 1]:
                    break
                if k == 4:
                    largest = i*j

    print(largest)
