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
    iterator2 = 0
    while (iterator2!=2):
        iterator = -1
        while (iterator!=len(array)):
            array[iterator],temp = temp,array[iterator]
            iterator += 1
        iterator2 += 1
    return array
