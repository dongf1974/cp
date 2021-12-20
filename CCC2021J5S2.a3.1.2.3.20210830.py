#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              CCC2021J5S2.a3.py
#
#    Version:                1.2
#
#    Build:                  3
#
#    Author:                 Dong Fang (Walter Dong)
#
#    Contact:                dongfang@ustc.edu
#                            dongf@live.com
#
#    Time:                   2021/08/30-2021/08/30 (1.0)
#                            2021/08/30-2021/08/30 (1.1)
#                            2021/08/30-2021/08/30 (1.2)
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

even_row_count = 0
odd_row_count = 0
for cell in row :
	if cell%2==0 :
		even_row_count += 1
	else :
		assert cell%2!=0
		odd_row_count += 1

even_column_count = 0
odd_column_count = 0
for cell in column :
	if cell%2==0 :
		even_column_count += 1
	else :
		assert cell%2!=0
		odd_column_count += 1

golden_count = even_row_count*odd_column_count+odd_row_count*even_column_count
print(golden_count)

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of CCC2021J5S2.a3.py
#
#\*_________________________________________________________*/
