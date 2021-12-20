#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              CCC2016J3.py
#
#    Version:                1.0
#
#    Build:                  3
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
# CCC 2016 Problem J3: Hidden Palindrome
# http://cemc.uwaterloo.ca/contests/computing/2016/index.html
#

def is_palindrome(word, start, end) :
	assert start<end
	left = start
	right = end-1
	while left<right :
		if word[left]!=word[right] :
			return False
		left += 1
		right -= 1
	return True

word = input()
word_length = len(word)

longest_palindrome_length = 1
for index in range(word_length-1) :
	start = index
	end = word_length
	if start+longest_palindrome_length>=end :
		break
	while start+longest_palindrome_length<end :
		if is_palindrome(word, start, end) :
			break
		end -= 1
	palindrome_length = end-start
	if palindrome_length>longest_palindrome_length :
		longest_palindrome_length = palindrome_length

print(longest_palindrome_length)

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of CCC2016J3.py
#
#\*_________________________________________________________*/
