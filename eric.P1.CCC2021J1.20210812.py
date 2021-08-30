#
# Author: Eric Zhang
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
