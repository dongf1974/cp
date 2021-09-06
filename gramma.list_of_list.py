#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              list_of_list.py
#
#    Version:                1.0
#
#    Build:                  1
#
#    Author:                 Dong Fang (Walter Dong)
#
#    Contact:                dongfang@ustc.edu
#                            dongf@live.com
#
#    Time:                   2021/09/05-2021/09/05 (1.0)
#
#    Notice:
#    Copyright (C) 2021, Dong Fang (Walter Dong).
#    All rights reserved.
#
#    This software is PROPRIETARY and CONFIDENTIAL. To get license,
#    contact Dong Fang (Walter Dong).
#-
#\*_________________________________________________________*/

n = int(input())
a = [0 for i in range(n)]
print(a)
#
# 3
#
# [0, 0, 0]
#

n = int(input())
a = [1 for i in range(n)]
print(a)
#
# 3
#
# [1, 1, 1]
#

n = int(input())
a = [i for i in range(n)]
print(a)
#
# 3
#
# [0, 1, 2]
#

n = int(input())
a = [i+1 for i in range(n)]
print(a)
print(a[2])
#
# 3
#
# [1, 2, 3]
# 3
#

n = int(input())
a = [[] for i in range(n)]
print(a)
a[2].append(1)
print(a)
#
# 3
#
# [[], [], []]
# [[], [], [1]]
#

n = int(input())
a = [[0, 0, 0, 0] for i in range(n)]
print(a)
a[0][1] = 6
print(a)
#
# 3
#
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# [[0, 6, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
#

n = int(input())
m = int(input())
a = [[0 for j in range(m)] for i in range(n)]
print(a)
a[1][2] = 6
a[n-1][m-1] = 4
print(a)
#
# 3
# 5
#
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# [[0, 0, 0, 0, 0], [0, 0, 6, 0, 0], [0, 0, 0, 0, 4]]
#

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of list_of_list.py
#
#\*_________________________________________________________*/
