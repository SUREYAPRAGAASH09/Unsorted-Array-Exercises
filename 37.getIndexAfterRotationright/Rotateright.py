def swapRight(array,shiftValue):
    if (shiftValue > len(array)):
        shiftValue = shiftValue - len(array)
    
    temp = 0
    j = 0
    while (j!=shiftValue):
        i = -1
        while (i!=len(array)):
            array[i],temp = temp,array[i]
            i += 1
        j += 1
    return array