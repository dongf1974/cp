#
# Author: Micheal Wu
#

#
# input:
#     <a, b>
#
# output:
#     gcd(a, b)
#
# note:
#     Euclidean algorithm
#

a=int(input())
b=int(input())
d=gcd(a,b)
print(d)

def gcd(a,b):
  r=a%b
  if r==0:
    gcd=b
    break
  if r!=0:
    a=b
    b=r
    gcd=gcd(a,b)
