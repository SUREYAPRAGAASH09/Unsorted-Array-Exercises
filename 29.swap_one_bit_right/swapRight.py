Question :
==========
    Rotste Right hand side Single bit at a time 
Input :
=======
    Unsorted Integer Array 
Output :
========
    Unsorted integer Array - After shifting the element right hand side 
Code :
=======
def swapRight(array):
    temp = 0
    shiftOperator = 0
    while (shiftOperator!=1):
        iterator = -1
        while (iterator!=len(array)):
            array[iterator],temp = temp,array[iterator]
            iterator += 1
        shiftOperator += 1
    return array
