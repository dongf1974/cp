#
# Author: Eric Zhang
# Reviewer: Dong, Fang
#

#
# input:
#     <line count>
#
# output:
#     *
#     **
#     ...
#     **...*
#

n=int(input(""))
j=0
for i in range(n):
	for j in range(j+1):
		print("*",end="")
		j=j+1
	print("")

#
# problem: logic of duloop
#             logic error (temporary fix)
# problem: coding style
#             meaningful naming (no fix)
# problem: usage of print()
#             input() VS input("")
# problem: usage of print()
#             print() VS print("")
#

n=int(input())
j=0
for i in range(n):
	for k in range(j+1):
		print("*",end="")
	print()
	j=j+1

#
# TODO: logic of duloop
# TODO: abstract function to avoid duloop
#
