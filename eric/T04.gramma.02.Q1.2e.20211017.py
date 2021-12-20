#
# Author: Eric Zhang
#

#
# input
#     <s> (is text)
#     <n> <m> (both are integer)
# output
#     <m characters of s, start from the No. n character>
# note
#     1. The first character is the No. 0 character.
#

s=input("")
m=int(input(""))
n=int(input(""))
for i in range(m+1):
    print(s[n+i+1],end="")
