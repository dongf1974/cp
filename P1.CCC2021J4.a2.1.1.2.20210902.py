#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              CCC2021J4.a2.py
#
#    Version:                1.1
#
#    Build:                  2
#
#    Author:                 Dong Fang (Walter Dong)
#
#    Contact:                dongfang@ustc.edu
#                            dongf@live.com
#
#    Time:                   2021/08/29-2021/08/29 (1.0)
#                            2021/09/02-2021/09/02 (1.1)
#
#    Notice:
#    Copyright (C) 2021, Dong Fang (Walter Dong).
#    All rights reserved.
#
#    This software is PROPRIETARY and CONFIDENTIAL. To get license,
#    contact Dong Fang (Walter Dong).
#-
#\*_________________________________________________________*/

#
# CCC 2021 Problem J4: Arranging Books
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

books = input()

L = books.count("L")
M = books.count("M")
S =  books.count("S")
assert L+M+S==len(books)

Ll = books.count("L", 0, L)
Lm = books.count("M", 0, L)
Ls = books.count("S", 0, L)
assert Ll+Lm+Ls==L

Ml = books.count("L", L, L+M)
Mm = books.count("M", L, L+M)
Ms = books.count("S", L, L+M)
assert Ml+Mm+Ms==M

Sl = books.count("L", L+M, L+M+S)
Sm = books.count("M", L+M, L+M+S)
Ss = books.count("S", L+M, L+M+S)
assert Sl+Sm+Ss==S

assert Ll+Ml+Sl==L
assert Lm+Mm+Sm==M
assert Ls+Ms+Ss==S

swap_LM = min(Lm, Ml)
swap_LS = min(Ls, Sl)
swap_MS = min(Ms, Sm)

swap_LMS = Lm+Ml-swap_LM*2
assert swap_LMS==Ls+Sl-swap_LS*2
assert swap_LMS==Ms+Sm-swap_MS*2

swap_count = swap_LM+swap_LS+swap_MS+swap_LMS*2
print(swap_count)

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of CCC2021J4.a2.py
#
#\*_________________________________________________________*/
