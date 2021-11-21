#
# Author: Eric Zhang
# Reviewer: Dong, Fang
#

#
# input
#     <n> <m> (both are integer)
# output
#     <n>
#     <n+1>
#     ...
#     <m>
#

mm=input("").split()
n=int(nm[0])
m=int(nm[1])
if m>=n:
    while n!=m:
        print(n)
        n=n+1
    print(m)
else:
    print("Error")
