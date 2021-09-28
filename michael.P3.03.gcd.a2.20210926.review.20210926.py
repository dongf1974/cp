#
# Author: Micheal Wu
# Reviewer: Dong, Fang
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

def gcd(a, b) :
  r=a%b
  if r==0:
    gcd=b
    break
  if r!=0:
    a=b
    b=r
    gcd=gcd(a,b)

#
# problem: how to return value in function
#

a=int(input())
b=int(input())
d=gcd(a,b)
print(d)

def gcd(a,b):
  r=a%b
  if r==0:
    return b
  if r!=0:
    a=b
    b=r
    return gcd(a,b)

#
# improvement: how to call recursively
#                 need not change vaule of a, b
#

a=int(input())
b=int(input())
d=gcd(a,b)
print(d)

def gcd(a,b):
  r=a%b
  if r==0:
    return b
  if r!=0:
    return gcd(b,r)

#
# improvement: usage of 'if...else', 'assert'
#

a=int(input())
b=int(input())
d=gcd(a,b)
print(d)

def gcd(a,b):
  r=a%b
  if r==0:
    return b
  else:
    assert r!=0
    return gcd(b,r)
