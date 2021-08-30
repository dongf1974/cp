#
# Author: Eric Zhang
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
