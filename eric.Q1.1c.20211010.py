#
# Author: Eric Zhang
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

mm=input("")
n=int(nm[0])
m=int(nm[2])
if n%2 or m%2 != 0:
    m=m-1
if m:
    while n!=m:
        print(n)
        n=n+2
    print(m)
else:
    print("Error")
