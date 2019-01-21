def shiftLeft(array,shiftValue):
    if (shiftValue > len(array)):
        shiftValue = shiftValue - len(array)
    i = 0
    while(i!=shiftValue):
        j = 0
        temp = (array[j])
        array.remove(array[j])
        array.append(temp)
        i+=1
    return array
