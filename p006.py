# https://projecteuler.net/problem=6

if __name__ == '__main__':
    sum_of_squares = 0
    for i in range(1, 101):
        sum_of_squares += i*i
    square_of_sum = sum(range(1, 101))**2
    print(square_of_sum-sum_of_squares)
