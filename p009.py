# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

if __name__ == '__main__':
    final_m = 0
    final_n = 0
    for m in range(1, 23):
        n = (500-m*m)/m
        if m < n or not n.is_integer():
            continue
        n = int(n)
        break
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    print(a, "*", b, "*", c, "=", a*b*c)
