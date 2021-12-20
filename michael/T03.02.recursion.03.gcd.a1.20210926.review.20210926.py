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
temp=0
if b>a:
  temp=a
  a=b
  b=temp

def gcd(a,b):
  while True:
    r=a%b
    if r==0:
      print(b)
      break
    if r!=0:
      b=r

#
# problem: how to define function, and call function
#

a=int(input())
b=int(input())
d=gcd(a,b)
print(d)

temp=0
if b>a:
  temp=a
  a=b
  b=temp

def gcd(a,b):
  while True:
    r=a%b
    if r==0:
      return b
    if r!=0:
      b=r

#
# problem: the logic is not Euclidean algorithm exactly
#             gcd(a,b)=gcd(b,r)
#

a=int(input())
b=int(input())
d=gcd(a,b)
print(d)

temp=0
if b>a:
  temp=a
  a=b
  b=temp

def gcd(a,b):
  while True:
    r=a%b
    if r==0:
      return b
    if r!=0:
      a=b
      b=r

#
# improvement: need not swap a, b
#

a=int(input())
b=int(input())
d=gcd(a,b)
print(d)

def gcd(a,b):
  while True:
    r=a%b
    if r==0:
      return b
    if r!=0:
      a=b
      b=r

#
# improvement: usage of 'if...else', 'assert'
#

a=int(input())
b=int(input())
d=gcd(a,b)
print(d)

def gcd(a,b):
  while True:
    r=a%b
    if r==0:
      return b
    else:
      assert r!=0
      a=b
      b=r

#
# improvement: logic of 'while' loop
#

a=int(input())
b=int(input())
d=gcd(a,b)
print(d)

def gcd(a,b):
  r=a%b
  while r!=0:
    a=b
    b=r
    r=a%b
  return b
