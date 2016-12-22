# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


# Cheat: 998001 is the largest product of two 3 digit integers

import datetime

def isPalindrome(n):
    text = str(n)
    return text == text[::-1]


def factor3(n):
    for f in range(999, 499, -1):
        f2 = n//f
        if(n % f == 0 and len(str(f2)) == 3):
            return [f, f2]
    return []


print(datetime.time())
for n in range(998001, 10000, -1):
    if(isPalindrome(n)):
        factors = factor3(n)
        if(len(factors) > 0):
            print(factors)
            print(n)
            print(datetime.time())
            break

print('none found')
