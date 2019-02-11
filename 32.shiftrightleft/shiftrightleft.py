Question :
==========
    Shift Right Left the element of the array
Input :
=======
    Unsorted Integer Array
Output :
========
    Unsorted Integer Array but, after shifting right left the element of the array
Code :
======
def swapRight(array,shiftValue):
    temp = 0
    iterator = 0
    while (iterator2!=shiftValue):
        iterator = -1
        while (iterator!=len(array)):
            array[iterator],temp = temp,array[iterator]
            iterator += 1
        iterator2 += 1
    return array

def shiftLeft(array,shiftValue):
    iterator = 0
    while(iterator!=shiftValue):
        iterator2 = 0
        temp = (array[iterator2])
        array.remove(array[iterator2])
        array.append(temp)
        iterator+=1
    return array

