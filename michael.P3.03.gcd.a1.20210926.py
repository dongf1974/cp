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

def gcd(a, b):
  while True:
    r=a%b
    if r==0:
      print(b)
      break
    if r!=0:
      b=r
