#31. Given an unsorted
#  integer array as input, rotate the contents of the array to the right by 2 positions.

def swapRight(array):
    
    
    temp = 0
    j = 0
    while (j!=2):
        i = -1
        while (i!=len(array)):
            array[i],temp = temp,array[i]
            i += 1
        j += 1
    return array

array = [5,7,6,9,2,8]
print(array)
print(swapRight(array))