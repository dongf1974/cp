#
# Author: Eric Zhang
# Reviewer: Dong, Fang
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

#
# problem: redundancy logic
#             'else'
# problem: coding style
#             naming
# problem: complexity
#             algrithm to reduce complexity (no code)
#

loop=int(input())
people=[]
bid=[]
for i in range(loop):
    name=input()
    amount=int(input())
    people.append(name)
    bid.append(amount)
sorted_bid=sorted(bid)
highest_bid=sorted_bid[loop-1]
for i in range(loop):
    if bid[i] == highest_bid:
        place=i
        break
print(people[place])

#
# TODO: algrithm to reduce complexity
#
