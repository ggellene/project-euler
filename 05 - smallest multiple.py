# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import sys


def remove_factors(array):
    for n in array[::-1]:
        for (i, x) in enumerate(array):
            if n % x == 0 and n != x:
                array.pop(i)
    return array


def is_multiple(multiple, factor):
    return multiple % factor == 0

maximum = int(sys.argv[1])
factors = remove_factors(list(range(2, maximum+1)))
upperBound = 1

for n in factors:
    upperBound *= n

print('testing factors {0} with upper bound {1}'.format(factors, upperBound))

space = range(upperBound, maximum, -maximum*(maximum-1))
index = 1
while index < len(space):
    multiple = space[index]
    isMultiple = True
    for test in factors[::-1]:
        if not is_multiple(multiple, test):
            isMultiple = False
            break
    if isMultiple:
        upperBound -= multiple
        space = range(upperBound, maximum, -maximum * (maximum - 1))
        print('new upper bound {0}'.format(upperBound))
        index = 0
    index += 1

print(upperBound)