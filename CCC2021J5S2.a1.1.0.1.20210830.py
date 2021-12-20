#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              CCC2021J5S2.a1.py
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
#    Time:                   2021/08/30-2021/08/30 (1.0)
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

canvas = [[0 for index_column in range(column_count)] for index_row in range(row_count)]

for index in range(choice_count) :
	choice = input()
	term = choice.split()
	direction = term[0]
	position = int(term[1])-1

	if direction=="R" :
		row = position
		for column in range(column_count) :
			canvas[row][column] += 1
	else :
		assert direction=="C"
		column = position
		for row in range(row_count) :
			canvas[row][column] += 1

golden_count = 0
for row in canvas :
	for cell in row :
		if cell%2!=0 :
			golden_count += 1

print(golden_count)

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of CCC2021J5S2.a1.py
#
#\*_________________________________________________________*/
