Problem Statement :
====================
    Given an unsorted integer array A, find the value that will be in 3rd position or index after 2 rotations to the left.
Input :
=======
    An Unsorted Integer Array ,
    Index Value - Type Integer,
    Rotation Value - Type Integer
Output :
========
    Get integer after left rotation is made by passing the index value 
Code :
======
import shiftLeft

def getIndexAfterrotationLeft(array,index,rotation_value):
    afterRotation = shiftLeft.shiftLeft(array,rotation_value)
    return afterRotation[index]
