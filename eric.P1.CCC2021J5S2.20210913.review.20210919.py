#
# Author: Eric Zhang
# Reviewer: Dong, Fang
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

#
# problem: logic about range
#             column or row
# problem: logic error, gramma
#             list of list, init and access, use different order
# problem: logic error
#             '== 0' or '== 1'
# problem: logic error
#             "C" vs "E"
# problem: logic error
#             missing output
# problem: coding style
#             style of "=", should be consist
# problem: coding style
#             meaningful naming
#

row = int(input())
column = int(input())
amount = int(input())

spread = [[0 for index_column in range(column)] for index_row in range(row)]

for i in range(amount):
    command = input()
    parts = command.split()
    direction = parts[0]
    point = parts[1]

    if direction == ("R"):
        for c in range(column):
            spread[point][c] += 1

    if direction == ("C"):
        for r in range(row):
            spread[r][point] += 1

count = 0
for c in range(column):
    for r in range(row):
        if spread[r][c] % 2 == 1:
            count += 1

print(count)
