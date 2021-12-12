#
# Author: Micheal Wu
# Reviewer: Dong, Fang
#

#
# CCC 2021 Problem J1: Boiling Water
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

n=int(input())
a=5*n-400
print(a)
if a>100:
	print(-1)
if a==100:
	print(0)
else:
	print(1)

#
# problem: logic error
#             wrong variable
# problem: logic error
#             'if...elif...else'
# problem: coding style
#             meaningful naming (no fix)
#

n=int(input())
a=5*n-400
print(a)
if n>100:
	print(-1)
elif n==100:
	print(0)
else:
	print(1)

#
# follow the naming in question (meaningful naming is better)
#

B=int(input())
P=5*B-400
print(P)
if B>100:
	print(-1)
elif B==100:
	print(0)
else:
	print(1)
