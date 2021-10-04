#
# Author: Eric Zhang
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
