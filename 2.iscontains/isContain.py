Question :
===========
    To find the element whether it is present or not 
Input :
=======
    Unsorted Integer Array 
Output :
=========
   True - If element present in the array 
   False - If elemnet is not present in the arrray
Code :
======
    def find_element(array,search_element):
    for iteratorValue in array:
        flag = False
        if (iteratorValue==search_element):
            flag = True
            break
    return flag
