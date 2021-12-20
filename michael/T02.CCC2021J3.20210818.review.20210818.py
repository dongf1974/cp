#
# Author: Micheal Wu
# Reviewer: Dong, Fang
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


#
# problem: logic of 'while' loop
#             how to 'break'
# problem: redundancy logic
#             remove 'previous'
# problem: logic error
#             direction == ...
# problem: logic error
#             sequence[2:] (no fix)
# problem: gramma
#             miss ':' at the end of 'if'
# problem: coding style
#             meaningful naming of 'a' (no fix)
#

direction = ""
while True:
    sequence = input()
    if sequence == "99999":
        break
    a=int(sequence[0]) + int(sequence[1])
    if a!=0:
        if a%2 == 0:
            direction = "right"
        else:
            direction = "left"
    print(direction + " " + sequence[2:])

#
# END
#
