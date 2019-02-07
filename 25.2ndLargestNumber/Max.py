 # To find the max of dictionary values 
 Problem :
=========
      To find the maximum element of dictionary values

Input :
=======
    Unsorted Array Elements - List

Output :
========
    Maximum Element in an Unsorted Array - integer

 Code :
======
import FindLenght
def findMaxrray):
    Array_lenght = FindLenght.len(values) 
    if (Array[0] < Array[1]): 
        Updated_maximum = array[0]
    else: 
        Updated_maximum = Array[1]
    iterator = 2 
    while(iterator!=Array_lenght): 
        if (Array[iterator]<Updated_maximum): 
            Updated_maximum = Array[iterator] 
        iterator += 1 
    return Updated_maximum
