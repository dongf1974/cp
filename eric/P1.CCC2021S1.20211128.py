#
# Author: Eric Zhang
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
