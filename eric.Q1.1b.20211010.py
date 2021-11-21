#
# Author: Eric Zhang
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

mm=input("")
n=int(nm[0])
m=int(nm[2])
if m:
    while n!=m:
        print(n)
        n=n+1
    print(m)
else:
    print("Error")
