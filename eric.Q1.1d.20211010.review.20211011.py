#
# Author: Eric Zhang
# Reviewer: Dong, Fang
#

#
# input
#     <n> <m> (both are integer)
# output
#     <n>
#     <n-3>
#     ...
#     <m> / or <m+1> / or <m+2>
#

mm=input("").split()
n=int(nm[0])
m=int(nm[1])
while not n<m:
    print(n)
    n=n-3
