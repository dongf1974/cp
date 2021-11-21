#
# Author: Eric Zhang
# Reviewer: Dong, Fang
#

#
# input
#     <n> <m> (both are integer)
# output
#     [[0, 1, ..., <m-1>], [0, 1, ..., <m-1>], ..., [0, 1, ..., <m-1>]]
# note
#     4. Generate list of list, the list has n elements, that each element is also a list, and is a list with m elements, the value of each element is 1, 2, ..., m-1.
#

n=int(input(""))
m=int(input(""))
list=[]
for i in range(n):
    inList=[]
    for i in range(m):
        inList.append[i]
    list.append[inList]
