Question :
==========
    15. Write a function that takes two unsorted integer arrays as input and  returns True if the two arrays are the same.
Input :
=======
    Unsorted Array Elements
Output :
========
    If two array element is same set flag to Ture other than set flag to False

import FindLenght
def compareTwoArrayElements(array1,array2):
    index = 0
    flag = False
    check = 0
    lenght_of_array1 = FindLenght.count(array1)
    lenght_of_array2 = FindLenght.count(array2)
    if (lenght_of_array1 == lenght_of_array2):     # this program will work only for two array with same lenght 
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
