#
# Author: Micheal Wu
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

n=int(input())
for i in range(n):
	print()
	for j in range(i+1):
		print("*", end = "")

#
# problem: logic of print()
#             first line of output is empty
#             last line of output may be blocked (held) in output buffer
# problem: coding style
#             meaningful naming (no fix)
# problem: coding style
#             style of '='
#

n = int(input())
for i in range(n):
	for j in range(i+1):
		print("*", end="")
	print()
