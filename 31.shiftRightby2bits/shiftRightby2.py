Question :
==========
      Given an unsorted integer array as input, rotate the contents of the array to the right by 2 positions.
Input :
=======
    Unsorted Integer Array 
Output :
========
    Unsorted Integer Array but, after shifting right hand side twice
Code :
======
def swapRight(array):
    temp = 0
    shiftValue = 0
    while (shiftValue!=2):
        iteratorValue = -1
        while (iteratorValue!=len(array)):
            array[iteratorValue],temp = temp,array[iteratorValue]
            iteratorValue += 1
        shiftValue += 1
    return array
