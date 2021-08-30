#
# Author: Eric Zhang
#

#
# input:
#     <line count>
#
# output:
#          *
#         ***
#         ...
#     **...*...**
#

n=int(input(""))
for i in range(n):
	for i in range(n-1):
		print(" ",end="")
	for j in range(j+1):
		print("* ",end="")
		j=j+1
	n=n-1
	print("")
