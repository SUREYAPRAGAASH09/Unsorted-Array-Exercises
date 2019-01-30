#37. Given an unsorted integer array A, 
# find the value that will be in 3rd position or index after 2 rotations to the right.
import Rotateright

def getIndexAfterrotationRight(array,index,rotation_value):
    afterRotation = Rotateright.swapRight(array,rotation_value)
    return afterRotation[index]

#array = [5,7,6,9,2,8]
#index = int(input("Enter the index value"))
#rotation_value = int(input("Enter the rotation value"))
#rint(getIndexAfterrotationRight(array,index,rotation_value))