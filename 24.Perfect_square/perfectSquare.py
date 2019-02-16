Question :
==========
    Given an unsorted integer array as input,  return the number of perfect squares in it.
Input :
=======
    unsorted Integer Array 
Output :
========
    Getting the list of perfect square number  
Code :
=======
import math
def isPerfectSquare(N):
    flag = False
    getSqrtN = math.sqrt(N)
    roundSqrtValue = round(M)
    if ((getSqrtN-roundSqrtValue)==0):
        flag = True
    return flag


def filterPerfectSquare(array):
    perfectSquareList = []
    for iteratorValue in array:
        if (perfectSquare(iteratorValue)):
            perfectSquareList.append(iteratorValue)
    return perfectSqareList
             

