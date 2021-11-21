#
# Author: Eric Zhang
#

#
# input
#     <s> (is text)
#     <n> <m> (both are integer)
# output
#     <characters of s, start from the No. n character, end BEFORE the No. m character>
# note
#     1. The first character is the No. 0 character.
#

s=input("")
n=int(input(""))
m=int(input(""))
print(s[n:m-1])
