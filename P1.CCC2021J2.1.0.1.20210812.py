#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              CCC2021J2.py
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
#    Time:                   2021/08/12-2021/08/12 (1.0)
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
# CCC 2021 Problem J2: Silent Auction
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

bid_count = int(input())

highest_bid = 0
winner = None
for index in range(bid_count) :
	name = input()
	amount = int(input())
	if amount>highest_bid :
		highest_bid = amount
		winner = name

print(winner)

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of CCC2021J2.py
#
#\*_________________________________________________________*/
