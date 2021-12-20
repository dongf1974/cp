#
# Author: Eric Zhang
# Reviewer: Dong, Fang
#

#
# CCC 2021 Problem S1: Crazy Fencing
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

n = int(input(""))
total=0
if n < 100000:
    height = input("")
    width = input("")
    heigth=height.split()
    width=width.split()
    for i in range(n):
       total=total+int(2/(int(width[i])+int(height[i])+int(height[i+1])))
    print(total)

#
# problem: type error 'heigth'
# problem: area fomular error
#

n = int(input(""))
total=0
if n < 100000:
    height = input("")
    width = input("")
    height=height.split()
    width=width.split()
    for i in range(n):
       height1 = int(height[i])
       height2 = int(height[i+1])
       width = int(width[i])
       fence = (height1+height2)*width/2
       total=total+s
    print(total)
