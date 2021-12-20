#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              CCC2016J2.a2.py
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
#    Time:                   2021/12/12-2021/12/12 (1.0)
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
# CCC 2016 Problem J2: Magic Squares
# http://cemc.uwaterloo.ca/contests/computing/2016/index.html
#

new_row = list(map(int, input().split()))
assert len(new_row)==4

total = 0
for number in new_row :
	total += number

column_total = [0 for column in range(4)]
for column in range(4) :
	column_total[column] += new_row[column]

magic = True

for row in range(1, 4) :
	new_row = list(map(int, input().split()))
	assert len(new_row)==4
	current_total = 0
	for column in range(4) :
		number = new_row[column]
		current_total += number
		column_total[column] += number
	if current_total!=total :
		magic = False
		break

if magic :
	for current_total in column_total :
		if current_total!=total :
			magic = False
			break

if magic :
	print("magic")
else :
	print("not magic")

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of CCC2016J2.a2.py
#
#\*_________________________________________________________*/
