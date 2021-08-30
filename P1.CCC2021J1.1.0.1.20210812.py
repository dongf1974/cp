#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              CCC2021J1.py
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
# CCC 2021 Problem J1: Boiling Water
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

temperature = int(input())
pressure = 5*temperature-400
print(pressure)
if temperature<100 :
	print(1)
elif temperature==100 :
	print(0)
else:
	assert temperature>100
	print(-1)

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of CCC2021J1.py
#
#\*_________________________________________________________*/
