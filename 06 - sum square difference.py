# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

import sys
import math

maximum = int(sys.argv[1])
space = range(1, maximum+1)


def sum_of_squares(iterable):
    result = 0
    for each in iterable:
        result += math.pow(each, 2)
    return int(result)


def square_of_sums(iterable):
    result = 0
    for each in iterable:
        result += each
    return int(math.pow(result, 2))

print(square_of_sums(space) - sum_of_squares(space))
