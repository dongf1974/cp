#
# Author: Eric Zhang
# Reviewer: Dong, Fang
#

#
# input
#     <s> (is text)
#     <n> <m> (both are integer)
# output
#     <number of lowercase characters of s>
#     <number of uppercase characters of s>
#     <number of lowercase characters of s, start from the No. n character, end BEFORE the No. m character>
#     <number of uppercase characters of s, start from the No. n character, end BEFORE the No. m character>
#     <s, to the characters start from the No. n character, end BEFORE the No. m character, all lowercase characters are transformed to uppercase>
# note
#     1. The first character is the No. 0 character.
#

s=input("")
m=int(input(""))
n=int(input(""))
upper=0
lower=0
upper1=0
lower1=0
for i in range(len(s)):
    if s[i] == upper(s[i]):
        upper+=1
    elif s[i] == lower(s[i]):
        lower+=1
new=s[n:m]
for j in range(len(new)):
    if new[j] == upper(new[j])
        upper1+=1
    elif new[j] == lower(new[j])
        lower1+=1
s=upper(s[n:m])
print(upper,upper1,lower,lower1)
print(s)
