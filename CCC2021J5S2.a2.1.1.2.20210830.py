#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              CCC2021J5S2.a2.py
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
#    Time:                   2021/08/30-2021/08/30 (1.0)
#                            2021/08/30-2021/08/30 (1.1)
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
# CCC 2021 Problem J5S2: Modern Art
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

row_count = int(input())
column_count = int(input())
choice_count = int(input())

row = [0 for index in range(row_count)]
column = [0 for index in range(column_count)]

for index in range(choice_count) :
	choice = input()
	term = choice.split()
	direction = term[0]
	position = int(term[1])-1

	if direction=="R" :
		row[position] += 1
	else :
		assert direction=="C"
		column[position] += 1

golden_count = 0
for index_row in range(row_count) :
	for index_column in range(column_count) :
		cell = row[index_row]+column[index_column]
		if cell%2!=0 :
			golden_count += 1

print(golden_count)

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of CCC2021J5S2.a2.py
#
#\*_________________________________________________________*/
