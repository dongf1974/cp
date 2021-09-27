#
# Author: Eric Zhang
#

#
# CCC 2021 Problem J5S2: Modern Art
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

row = int(input())
column = int(input())
amount = int(input())

spread = [[0 for index_column in range(column)] for index_row in range(row)]

for i in range(amount):
    command=input()
    parts=command.split()
    direction = parts[0]
    point = parts[1]

    if direction == ("R"):
        for j in range:
            spread[point][j]+=1

    if direction == ("E"):
        for k in range:
            spread[point][k]+=1

count=0
for s in range(column):
    for t in range(row):
        if spread[s][t] % 2 == 0:
            count+=1
