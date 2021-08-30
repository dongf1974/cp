#
# Author: Micheal Wu
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
