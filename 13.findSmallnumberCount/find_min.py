Problem :
=========
 To find the min of dictionary values
Input :
=======
    Unsorted Array Elements - List in Python
Output :
========
    Minimum Element in an Unsorted Array - Integer
 
Code :
======
import FindLenght
def findMin(Array):
    
    Array_lenght = FindLenght.len(values) 
     
    if (Array[0] < Array[1]): 
        Updated_minimum  = Array[0]
    else: 
        Updated_minimum = Array[1]
    iterator = 2 
    while(iterator!=Array_lenght): 
        if (Array[iterator]<Updated_minimum): 
            Updated_minimum = Array[iterator] 
        iterator += 1 
    return Updated_minimum 


