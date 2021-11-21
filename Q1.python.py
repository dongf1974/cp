#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              Q1.python.py
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
#    Time:                   2021/10/06-2021/10/06 (1.0)
#
#    Notice:
#    Copyright (C) 2021, Dong Fang (Walter Dong).
#    All rights reserved.
#
#    This software is PROPRIETARY and CONFIDENTIAL. To get license,
#    contact Dong Fang (Walter Dong).
#-
#\*_________________________________________________________*/

# ------------------------------------
# C1. range()
# ------------------------------------
# ------------------------------------
# (a) range(), start=0
# ------------------------------------

n = int(input())
assert n>=0

for i in range(n+1) :
    print(i)

# ------------------------------------
# (b) range(), start!=0
# ------------------------------------

tokens = input().split()
n = int(tokens[0])
m = int(tokens[1])
assert m>=n

for i in range(n, m+1) :
    print(i)

# ------------------------------------
# (c) range(), step>1
# ------------------------------------

tokens = input().split()
n = int(tokens[0])
m = int(tokens[1])
assert m>=n

for i in range(n, m+1, 2) :
    print(i)

# ------------------------------------
# (d) range(), step<0
# ------------------------------------

tokens = input().split()
n = int(tokens[0])
m = int(tokens[1])
assert m<=n

for i in range(n, m-1, -3) :
    print(i)



# ------------------------------------
# C2. string
# ------------------------------------
# ------------------------------------
# (a) sub string, left (first)
# ------------------------------------

s = input()
n = int(input())
assert n>0
assert n<=len(s)

print(s[:n])

# ------------------------------------
# (b) sub string, right
# ------------------------------------

s = input()
n = int(input())
assert n>=0
assert n<len(s)

print(s[n:])

# ------------------------------------
# (c) sub string, right (last)
# ------------------------------------

s = input()
n = int(input())
assert n>0
assert n<=len(s)

print(s[len(s)-n:])

# ------------------------------------
# (d) sub string, start and end
# ------------------------------------

s = input()
tokens = input().split()
n = int(tokens[0])
m = int(tokens[1])
assert n>=0
assert n<len(s)
assert m>n
assert m<=len(s)

print(s[n:m])

# ------------------------------------
# (e) sub string, start and length
# ------------------------------------

s = input()
tokens = input().split()
n = int(tokens[0])
m = int(tokens[1])
assert n>=0
assert n<len(s)
assert m>0
assert m<=len(s)-n

print(s[n:n+m])

# ------------------------------------
# (f) character, loop, ASCII
# ------------------------------------

s = input()
tokens = input().split()
n = int(tokens[0])
m = int(tokens[1])
assert n>=0
assert n<len(s)
assert m>n
assert m<=len(s)

lowercase = 0
uppercase = 0
for c in s :
    if c>='a' and c<='z' :
        lowercase = lowercase+1
    elif c>='A' and c<='Z' :
        uppercase = uppercase+1
print(lowercase)
print(uppercase)

lowercase = 0
uppercase = 0
for c in s[n:m] :
    if c.islower() :
        lowercase = lowercase+1
    elif c.isupper() :
        uppercase = uppercase+1
print(lowercase)
print(uppercase)

sub = s[n:m]
s = s[:n] + sub.upper() + s[m:]
print(s)

# ------------------------------------
# C3. list
# ------------------------------------
# ------------------------------------
# (a) list, init with zero
# ------------------------------------

n = int(input())
assert n>0

l = [0 for i in range(n)]
print(l)

# ------------------------------------
# (b) list, init with some regular
# ------------------------------------

n = int(input())
assert n>0

l = [i for i in range(n)]
print(l)

# ------------------------------------
# (c) list, init with some regular
# ------------------------------------

n = int(input())
assert n>0

l = [i+1 for i in range(n)]
print(l)

# ------------------------------------
# (d) list of list, init with empty list
# ------------------------------------

n = int(input())
assert n>0

l = [[] for i in range(n)]
print(l)

# ------------------------------------
# (e) list of list, init with 0
# ------------------------------------

tokens = input().split()
n = int(tokens[0])
m = int(tokens[1])
assert n>0
assert m>0

l = [[0 for j in range(m)] for i in range(n)]
print(l)

# ------------------------------------
# (f) list of list, init with some regular
# ------------------------------------

tokens = input().split()
n = int(tokens[0])
m = int(tokens[1])
assert n>0
assert m>0

l = [[j for j in range(m)] for i in range(n)]
print(l)

# ------------------------------------
# (g) list of list, init with some regular
# ------------------------------------

tokens = input().split()
n = int(tokens[0])
m = int(tokens[1])
assert n>0
assert m>0

l = [[i for j in range(m)] for i in range(n)]
print(l)

# ------------------------------------
# (h) list of list, init with some regular
# ------------------------------------

tokens = input().split()
n = int(tokens[0])
m = int(tokens[1])
assert n>0
assert m>0

l = [[i+j+1 for j in range(m)] for i in range(n)]
print(l)
print(l[n-1][m-1])

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of Q1.python.py
#
#\*_________________________________________________________*/
