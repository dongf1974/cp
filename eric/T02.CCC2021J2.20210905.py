#
# Author: Eric Zhang
#

#
# CCC 2021 Problem J2: Silent Auction
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

loop=int(input(""))
best=""
highest=0
for i in range(loop):
    name=input("")
    bided=int(input(""))
    if bided > highest:
        highest = bided
        winner=name

print(winner)
