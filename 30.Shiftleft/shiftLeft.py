def shiftLeft(array):
    i = 0
    while(i!=1):
        j = 0
        temp = (array[j])
        array.remove(array[j])
        array.append(temp)
        i+=1
    return array

array = [5,7,6,9,2,8]
print(array)
print(shiftLeft(array))