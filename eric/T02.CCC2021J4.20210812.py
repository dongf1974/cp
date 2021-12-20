#
# Author: Eric Zhang
#

#
# CCC 2021 Problem J4: Arranging Books
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

line = input("Small to Large")
line=line[::-1]
nL= line.count("L")
nM = line.count("M")
nS = line.count("S")
#In the L pile count how many M and S
nL2M = line[nL:nM].count("M")
nL2S = line[nL:nS].count("S")
#In the M pile, count how many L and S
nM2L = line[nM:nL].count("L")
nM2S = line[nM:nS].count("S")
#In the S pile, count how many L and M
nS2L = line[nS:nL].count("L")
nS2M = line[nS:nM].count("M")
#The calculation for the minimum swap is
min_swap = min (nL2M, nM2L) + min (nL2S, nS2L) + min (nM2S, nS2M) + 2*abs(nL2M - nM2L)
print (min_swap)
