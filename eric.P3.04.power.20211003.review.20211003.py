#
# Author: Eric Zhang
# Reviewer: Dong, Fang
#

#
# input:
#     <a, n>
#
# output:
#     power(a, n) = a^n
#

def power(x, y):
    if y == 0:
        return 1
    if y >= 1:
        return x * power(x, y - 1)
print(power(4,2))

#
# problem: usage of 'if...else'
# problem: the complexity is O(n), not O(log n)
#             need change algorithm (no code)
#

def power(x, y):
    if y == 0:
        return 1
    else:
        assert y >= 1
        return x * power(x, y - 1)

print(power(4,2))
