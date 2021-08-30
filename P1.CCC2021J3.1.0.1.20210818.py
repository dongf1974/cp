#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              CCC2021J3.py
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
#    Time:                   2021/08/18-2021/08/18 (1.0)
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
# CCC 2021 Problem J3: Secret Instructions
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

direction = None
while True :
	instruction = input()
	if instruction=="99999" :
		break
	direction_flag = int(instruction[0])+int(instruction[1])
	if direction_flag!=0 :
		if direction_flag%2==0 :
			direction = "right"
		else :
			assert direction_flag%2!=0
			direction = "left"
	step = int(instruction[2:])
	print(direction, end=" ")
	print(step)

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of CCC2021J3.py
#
#\*_________________________________________________________*/
