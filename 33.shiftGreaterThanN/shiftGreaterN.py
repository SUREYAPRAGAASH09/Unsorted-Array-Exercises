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


array = [5,7,6,9,2,8]
shiftValue = 10
print(array)
print("Shift Right")
print("-------------------------")
print(swapRight(array,shiftValue))
print("Shift Left")
print("--------------------------")
array = [5,7,6,9,2,8]
print(shiftLeft(array,shiftValue))
