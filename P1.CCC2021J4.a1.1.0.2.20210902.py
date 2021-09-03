#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              CCC2021J4.a1.py
#
#    Version:                1.0
#
#    Build:                  2
#
#    Author:                 Dong Fang (Walter Dong)
#
#    Contact:                dongfang@ustc.edu
#                            dongf@live.com
#
#    Time:                   2021/08/29-2021/08/29 (1.0.1)
#                            2021/09/02-2021/09/02 (1.0.2)
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

L = 0
M = 0
S = 0
for book in books :
	if book=='L' :
		L += 1
	elif book=='M' :
		M += 1
	else :
		assert book=='S'
		S += 1
assert L+M+S==len(books)

Ll = 0
Lm = 0
Ls = 0
for index in range(L) :
	book = books[index]
	if book=='L' :
		Ll += 1
	elif book=='M' :
		Lm += 1
	else :
		assert book=='S'
		Ls += 1
assert Ll+Lm+Ls==L

Ml = 0
Mm = 0
Ms = 0
for index in range(L, L+M) :
	book = books[index]
	if book=='L' :
		Ml += 1
	elif book=='M' :
		Mm += 1
	else :
		assert book=='S'
		Ms += 1
assert Ml+Mm+Ms==M

Sl = 0
Sm = 0
Ss = 0
for index in range(L+M, L+M+S) :
	book = books[index]
	if book=='L' :
		Sl += 1
	elif book=='M' :
		Sm += 1
	else :
		assert book=='S'
		Ss += 1
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
#    End of CCC2021J4.a1.py
#
#\*_________________________________________________________*/
