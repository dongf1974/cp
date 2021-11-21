#
# Author: Eric Zhang
#

#
# input
#     <s> (is text)
#     <n> (is integer)
# output
#     <characters of s, start from the No. n character>
# note
#     1. The first character is the No. 0 character.
#

s=input("")
n=int(input(""))
print(s[n-1:])
