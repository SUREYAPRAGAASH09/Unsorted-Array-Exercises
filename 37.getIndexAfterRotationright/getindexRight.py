#37. Given an unsorted integer array A, 
# find the value that will be in 3rd position or index after 2 rotations to the right.
import Rotateright

def getIndexAfterrotationRight(array,index,rotation_value):
    afterRotation = Rotateright.swapRight(array,rotation_value)
    return afterRotation[index]

array = [5,7,6,9,2,8]
index = 3
rotation_value = 2
print(getIndexAfterrotationRight(array,index,rotation_value))