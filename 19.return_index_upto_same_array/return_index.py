Question :
===========
        Return the index upto the same array elements 
Input :
=======
        Unsorted array elements 
Output :
========
        Return index upto which same array elements 
    
Code :
======
def array12(array1,i):
    return array1[i]

def array13(array2,i):
    return array2[i]

#My Assumption :
===============
      this program works only for array elements having same size 
def return_index(array1,array2):
    flag = True
    iterator = 0
    while (flag):
        if ((array12(array1,iterator)) == (array13(array2,iterator))):
            print (iterator)
            iterator += 1
            flag = True
        else:
            flag = False
    return -1
