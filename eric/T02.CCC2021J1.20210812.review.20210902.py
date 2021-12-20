#
# Author: Eric Zhang
# Reviewer: Dong, Fang
#

#
# CCC 2021 Problem J1: Boiling Water
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

boil=int(input())
pressure=5*boil-400
print(pressure)
if pressure > 100:
    print("-1")
if pressure < 100:
    print("1")
if pressure == 100:
    print(0)

#
# problem: usage of 'if...elif...else'
# problem: usage of print()
#             print("1") VS print(1)
#             print("-1") VS print(-1)
#

boil=int(input())
pressure=5*boil-400
print(pressure)
if pressure > 100:
    print(-1)
elif pressure < 100:
    print(1)
else:
    print(0)

#
# END
#
