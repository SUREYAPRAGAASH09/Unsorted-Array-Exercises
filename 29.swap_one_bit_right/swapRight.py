def swapRight(array):
    
    
    temp = 0
    j = 0
    while (j!=1):
        i = -1
        while (i!=len(array)):
            array[i],temp = temp,array[i]
            i += 1
        j += 1
    return array
print("--------------------------") 
print()
array = [5,7,6,9,2,8]
print(array)
print(swapRight(array))
print("--------------------------")