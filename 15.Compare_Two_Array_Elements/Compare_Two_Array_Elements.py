#15. Write a function that takes two unsorted integer arrays as input and 
# returns True if the two arrays are the same.
import FindLenght
def compareArrayElements(array1,array2):
    index = 0
    flag = False
    check = 0
    lenght_of_array1 = FindLenght.count(array1)
    lenght_of_array2 = FindLenght.count(array2)
    if (lenght_of_array1 == lenght_of_array2):
        lenght = lenght_of_array1 
        while(index!=lenght):
            if ( array1[index] == array2[index] ):
                check = 1
            else:
                check = 0
                break 
            index += 1

    if check == 1 :
        flag = True
           

    return flag

array1 = [2,8,1,4,5,2]
array2 = [2,9,1,4,5]
print(compareArrayElements(array1,array2))