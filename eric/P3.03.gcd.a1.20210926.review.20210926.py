#
# Author: Eric Zhang
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

r=0
def gcd(a, b):
  while r != 0:
    if r = 0:
      break

    if a>b:
      r = a%b
    if b>a:
      r=b%a
  return(r)


gcd(7,5)
print(gcd)

#
# problem: how to call function
#

r = 0
def gcd(a, b):
  while r != 0:
    if r = 0:
      break

    if a>b:
      r = a%b
    if b>a:
      r=b%a
  return (r)

d = gcd(7,5)
print(d)

#
# problem: redundant logic of 'while' loop
#

r = 1
def gcd(a, b):
  while r != 0:
    if a>b:
      r = a%b
    if b>a:
      r = b%a
  return (r)

d = gcd(7,5)
print(d)

#
# problem: scope of 'r'
#

def gcd(a, b):
  r = 1
  while r != 0:
    if a>b:
      r = a%b
    if b>a:
      r = b%a
  return (r)

d = gcd(7,5)
print(d)

#
# problem: logic of gcd
#

def gcd(a, b):
  r = b
  while r != 0:
    r = a%b
    a = b
    b = r
  return (a)

d = gcd(7,5)
print(d)
