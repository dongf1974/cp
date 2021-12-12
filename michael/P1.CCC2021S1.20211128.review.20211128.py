#
# Author: Micheal Wu
# Reviewer: Dong, Fang
#

#
# CCC 2021 Problem S1: Crazy Fencing
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

m=int(input))
a=0
h=list(int, input.split())
w=list(int, input.split())
for i in range(m):
	a+=(h[i]+h[i+1])/2*w[i]
print(area)

#
# problem: grammar error
#             list(int, input.split())
# problem: output error
#             no fix
#

m=int(input))
a=0
h=list(map(int, input.split()))
w=list(map(int, input.split()))
for i in range(m):
	a+=(h[i]+h[i+1])/2*w[i]
print(area)
