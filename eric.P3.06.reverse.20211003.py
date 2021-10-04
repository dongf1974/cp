#
# Author: Eric Zhang
#

#
# input:
#     <abcd...> (abcd is integer)
#
# output:
#     <...dcba>
#

def reverse(n):
    return((n//10)+10*(n-n//10*10))
print(reverse(56))
