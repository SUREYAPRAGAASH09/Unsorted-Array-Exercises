#38. Given an unsorted integer array A, find the value that will be in 
# 3rd position or index after 2 rotations to the left.

import shiftLeft

def getIndexAfterrotationLeft(array,index,rotation_value):
    afterRotation = shiftLeft.shiftLeft(array,rotation_value)
    return afterRotation[index]

print("====================================================")

array = [5,7,6,9,2,8]
index = 3
rotation_value = 2
print(getIndexAfterrotationLeft(array,index,rotation_value))
print("======================================================")
   