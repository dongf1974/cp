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
temp=0
if b>a:
  temp=a
  a=b
  b=temp

def gcd(a,b):
  r=a%b
  if r==0:
    gcd=b
    break
  if r!=0:
    a=b
    b=r
    gcd=gcd(a,b)
