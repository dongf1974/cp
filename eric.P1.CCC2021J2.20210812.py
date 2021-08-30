#
# Author: Eric Zhang
#

#
# CCC 2021 Problem J2: Silent Auction
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

loop=int(input())
people=[]
bid=[]
for i in range(loop):
    person=input()
    bided=int(input())
    people.append(person)
    bid.append(bided)
sortedbid=sorted(bid)
highestbid=sortedbid[loop-1]
for counter in range(loop):
    if bid[counter] == highestbid:
        place=counter
        break
    else:
        continue
print(people[place])
