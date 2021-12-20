#
# Author: Eric Zhang
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
