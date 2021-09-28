#
# Author: Eric Zhang
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
def gcd(a, b) :
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
