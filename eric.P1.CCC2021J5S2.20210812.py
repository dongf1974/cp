#
# Author: Eric Zhang
#

#
# CCC 2021 Problem J5S2: Modern Art
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

m = int(input())
n = int(input())
k = int(input())
commands = []
for i in range(k):
    commands.append(input().split())
#print(commands)
result = [[0] * (n + 1) for i in range(m + 1)]
#print(result)
for i in range(k):
    if commands[i][0]==("R"):
        row = int(commands[i][1])-1
        for j in range(n):
            result[row][j]=(result[row][j]=1)%2
    else:
        col=int(commands[i][1])-1
        for k in range(m):
