Problem Statement :
====================
    Given an unsorted integer array A, find the value that will be in  3rd position or index after 2 rotations to the left.
Input :
=======
    Unsorted Integer Array
Output :
========
    Integer Element after rotation has performed.
Code :
======
import shiftLeft

def getIndexAfterrotationLeft(array,index,rotation_value):
    index = 3
    rotationValue = 2
    afterRotation = shiftLeft.shiftLeft(array)
    return afterRotation[index]
 
