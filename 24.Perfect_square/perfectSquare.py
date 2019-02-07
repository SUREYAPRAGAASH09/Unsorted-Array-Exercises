Question :
==========
    Given an unsorted integer array as input,  return the number of perfect squares in it.
Input :
=======
    unsorted Array 
Output :
========
    Getting the list of perfect square number  
Code :
=======
import math
def perfectSquare(N):
    flag = False
    getSqrtN = math.sqrt(N)
    roundSqrtValue = round(M)
    if ((getSqrtN-roundSqrtValue)==0):
        flag = True
    return flag


def filter_perfectSquare(array):
    for iterator in array:
        if (perfectSquare(iterator)):
            print (iterator)

