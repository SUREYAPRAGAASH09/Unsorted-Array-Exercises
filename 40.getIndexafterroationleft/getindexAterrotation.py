#38. Given an unsorted integer array A, find the value that will be in 
# 3rd position or index after 2 rotations to the left.

import shiftLeft

def getIndexAfterrotationLeft(array,index,rotation_value):
    afterRotation = shiftLeft.shiftLeft(array,rotation_value)
    return afterRotation[index]

#array = [5,7,6,9,2,8]
#index = int(input("Enter the index value"))
#rotation_value = int(input("Enter the rotation value"))
#print(getIndexAfterrotationLeft(array,index,rotation_value))