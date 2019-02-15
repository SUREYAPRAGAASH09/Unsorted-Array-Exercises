import FindLenght

def Equate(array):
    flag = NULL
    Lenght = FindLenght.count(array)
    firstElement = 0
    while (firstElement!=Lenght):
        check = array[firstElement]
        secondElement = firstElement+1
        while (secondElement!=Lenght):
            if (check == array[j]):
                flag = False
            else:
                flag = True
                break
            secondElement += 1
        firstElement += 1
 
    return flag
