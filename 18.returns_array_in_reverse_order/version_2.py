import FindLenght
def iseven(lenght):
    flag = False
    if lenght % 2 == 0:
        flag = True
    return flag
def inplace_reverse(array):
    lenght = FindLenght.count(array)
    if (not iseven(lenght)):
        lenght = lenght -1
    i = 1
    while(i!=(lenght/2)+1):
        array[i-1],array[-i] = array[-i],array[i-1]
        i += 1
    return array

array = [2,8,6,5,4,3]
print(array)
print(inplace_reverse(array))

