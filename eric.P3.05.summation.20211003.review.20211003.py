#
# Author: Eric Zhang
# Reviewer: Dong, Fang
#

#
# input:
#     <n>
#
# output:
#     <1+2+...+n>
#

def add(n):
    if n <= 1:
        return n
    else:
        return n + add(n-1)

print(add(10))

#
# improvement: stop condition, 'n <= 1'
#

def add(n):
    if n == 0:
        return 0
    else:
        return n + add(n-1)

print(add(10))
