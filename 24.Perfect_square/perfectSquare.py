#24.  Given an unsorted integer array as input,  return the number of perfect squares in it.
import math
def perfectSquare(N):
    flag = False
    M = math.sqrt(N)
    x = round(M)
    if ((M-x)==0):
        flag = True
    return flag

#print(perfectSquare(16))
def filter_perfectSquare(array):
    for i in array:
        if (perfectSquare(i)):
            print (i)

array = [24,16,90,25,75,64]
filter_perfectSquare(array)
