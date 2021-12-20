#
# Author: Eric Zhang
#

#
# input:
#     <line count>
#
# output:
#          *
#         **
#        ...
#     **...*
#

n=int(input(""))
g=0
j=0
for i in range(n):
	for j in range(n-1):
		print(" ",end="")
	for g in range(g+1):
		print("*",end="")
		g=g+1
	print("")
	n = n - 1
