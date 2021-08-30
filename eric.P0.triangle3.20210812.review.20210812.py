#
# Author: Eric Zhang
# Reviewer: Dong, Fang
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

#
# problem: logic of duloop
#             logic error
# problem: coding style
#             meaningful naming
#

#
# TODO: logic of duloop
# TODO: abstract function to avoid duloop
#
