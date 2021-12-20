#
# Author: Eric Zhang
#

#
# CCC 2021 Problem J3: Secret Instructions
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

step=0
place=0
while int(step) != 99999:
    step=input()
    if int(step)== 99999:
        break
    directionstep=int(step[0])+int(step[1])
    if int(directionstep)==0:
        if place==1:
            print("left ",step[2:])
        if place==0:
            print("right ",step[2:])
    if int(directionstep)/2 - int(int(directionstep)/2) != 0:
        print("left ",step[2:])
        place=1
    elif directionstep/2 == int(int(directionstep)/2) and directionstep != 0:
        print("right ",step[2:])
        place=0
