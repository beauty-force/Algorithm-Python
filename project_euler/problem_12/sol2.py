"""
Highly divisible triangular numbers
Problem 12
The sequence of triangle numbers is generated by adding the natural numbers. So
the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten
terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""
from __future__ import print_function


def triangle_number_generator():
    for n in range(1, 1000000):
        yield n * (n + 1) // 2


def count_divisors(n):
    return sum(
        [2 for i in range(1, int(n ** 0.5) + 1) if n % i == 0 and i * i != n]
    )


def solution():
    """Returns the value of the first triangle number to have over five hundred
    divisors.
    
    # The code below has been commented due to slow execution affecting Travis.
    # >>> solution()
    # 76576500
    """
    return next(
        i for i in triangle_number_generator() if count_divisors(i) > 500
    )


if __name__ == "__main__":
    print(solution())
