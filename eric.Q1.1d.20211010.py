#
# Author: Eric Zhang
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

mm=input("")
n=int(nm[0:2])
m=int(nm[3])
if m-1%3==0:
    m=m-1
if m-2%3==0:
    m=m-2
while not n<=m:
    print(n)
    n=n-3
print(m)
