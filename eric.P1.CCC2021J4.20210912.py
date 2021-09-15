#
# Author: Eric Zhang
#

#
# CCC 2021 Problem J4: Arranging Books
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

book=input()

# Counting the Values
l=book.count("L")
m=book.count("M")
s=book.count("S")

# Defining Varibles
Ll=0
Lm=0
Ls=0

# Counting Values in the L section
lBooks=book[0:l]
Ll=lBooks.count("L")
Lm=lBooks.count("M")
Ls=lBooks.count("S")

# Defining more Varibles
Ml=0
Mm=0
Ms=0

# Counting Values in the M section
mBooks=book[l:m]
Ml=mBooks.count("L")
Mm = mBooks.count("M")
Ms = mBooks.count("S")

# Last Defining of Varibles
Sl=0
Sm=0
Ss=0

# Counting Values in the S section
sBooks=book[0:l]
Sl=sBooks.count("L")
Sm = sBooks.count("M")
Ss = sBooks.count("S")

# Which is less?
swap1 = min(Lm, Ml)
swap2 = min(Ls, Sl)
swap3 = min(Ms, Sm)

# Either doing Lm-Ml, or Ml-Lm
swap4 = Lm+Ml-swap1*2

# Checking if all the Values are the same
if swap4==Ls+Sl-swap2*2 and swap4==Ms+Sm-swap3*2:

    # Adding up all the values
    swap_all=swap1+swap2+swap3+swap4*2

    # Print
    print(swap_all)
