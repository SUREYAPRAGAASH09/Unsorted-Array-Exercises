import FindLenght

def Equate(array):
    #flag = False
    Lenght = FindLenght.count(array)
    i = 0
    while (i!=Lenght):
        check = array[i]
        j = i+1
        while (j!=Lenght):
            if (check == array[j]):
                flag = False
            else:
                flag = True
                break
            j += 1
        i += 1
 
    return flag



#array = [1,1,1,1]
#array = [1,2,6,7]
#print(Equate(array))