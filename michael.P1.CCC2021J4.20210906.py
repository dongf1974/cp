#
# Author: Micheal Wu
#

#
# CCC 2021 Problem J4: Arranging Books
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

class section:
    l=0
    m=0
    s=0
    def add(self, book):
        if book == "L":
            l+=1
        if book == "M":
            l+=1
        if book == "S":
            l+=1
books = input()
total = Section()

for book in books:
    total.add(book)

l = Section()
M = Section()
S = Section()
j=0
for i in range(total.l):
    l.add(books[j])
    j += 1
for i in range(total.m):
    m.add(books[j])
    j += 1
for i in range(total.s):
    s.add(books[j])
    j += 1

print(l.m + l.s + m.l + m.s - min(m.l, l.m))
