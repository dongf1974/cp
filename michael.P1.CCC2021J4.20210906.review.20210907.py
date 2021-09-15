#
# Author: Micheal Wu
# Reviewer: Dong, Fang
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

#
# problem: gramma
#             'self' for member
# problem: gramma
#             class name 'section', 'Section'
# problem: gramma
#             variable name 'M', 'm'; 'S', 's'
# problem: logic error
#             'self.m', 'self.s'
# problem: logic
#             'if...elif...else'
# problem: complex logic of output
# problem: coding style
#             meaningful naming (no fix)
#

class Section:
    l=0
    m=0
    s=0
    def add(self, book):
        if book == "L":
            self.l+=1
        elif book == "M":
            self.m+=1
        elif book == "S":
            self.s+=1

books = input()
total = Section()

for book in books:
    total.add(book)

l = Section()
m = Section()
s = Section()
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

# print(l.m + l.s + m.l + m.s - min(m.l, l.m))

lm = min(l.m, m.l)
ls = min(l.s, s.l)
ms = min(m.s, s.m)
lms = max(l.m, m.l)-lm
# lms = max(l.s, s.l)-ls
# lms = max(m.s, s.m)-ms
print(lm+ls+ms+lms*2)
