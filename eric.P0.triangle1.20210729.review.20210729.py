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

x=int(input("Input A number:"))
y=1
for i in range(x)
	for j in range(y)
		print("*", end='')
	y=y+1

#
# problem: logic of duloop
#             how to (no fix)
# problem: usage of print()
#             output without 'new line' (end="")
# problem: usage of print()
#             output 'new line'
# problem: gramma
#             miss ':' at the end of 'for'
# problem: coding style
#             meaningful naming (no fix)
# problem: coding style
#             style of "" and '', should be consist
#

x=int(input("Input A number:"))
y=1
for i in range(x):
	for j in range(y):
		print("*", end="")
	y=y+1
	print()

#
# TODO: logic of duloop
#
