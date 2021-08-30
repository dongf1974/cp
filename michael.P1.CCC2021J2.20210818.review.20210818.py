#
# Author: Micheal Wu
# Reviewer: Dong, Fang
#

#
# CCC 2021 Problem J2: Silent Auction
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

n = int(input())
winner = ""
highest = 0
for i in range(n):
	name=input()
  bid=int(input())
  if bid > highest:
  	winner = name
    highest = bid

print(winner)

#
# problem: coding style
#             ' ' and 'TAB' mix in the beginning of line
#

n = int(input())
winner = ""
highest = 0
for i in range(n):
  name=input()
  bid=int(input())
  if bid > highest:
    winner = name
    highest = bid

print(winner)
