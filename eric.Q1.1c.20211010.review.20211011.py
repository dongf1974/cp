#
# Author: Eric Zhang
# Reviewer: Dong, Fang
#

#
# input
#     <n> <m> (both are integer)
# output
#     <n>
#     <n+2>
#     ...
#     <m> / or <m-1>
#

mm=input("").split()
n=int(nm[0])
m=int(nm[1])
if m>=n:
    while n<=m:
        print(n)
        n=n+2
else:
    print("Error")
