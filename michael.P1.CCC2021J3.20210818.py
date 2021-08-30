#
# Author: Micheal Wu
#

#
# CCC 2021 Problem J3: Secret Instructions
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

previous = ""
while True:
	sequence = input()
  a=int(sequence[0]) + int(sequence[1])
  direction = ""
  if a==0:
  	direction = previous
  elif a%2 == 0:
  	direction == "right"
  elif a%2 == 1:
  	direction == "left"
  if sequence == "99999"
    break
  print(direction + " " + sequence[2:])
  previous = direction
