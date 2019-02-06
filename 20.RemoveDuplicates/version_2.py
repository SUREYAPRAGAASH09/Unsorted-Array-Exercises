Question :
===========
    Remove Duplicate without using Dictionary Data Structure 
Input :
=======
    Unsorted Array Elements
Ouptut :
========
    Array Elements not having duplicate values in it 
Code :
=======
def removeDuplicate(array):
    iterator = 0
    newList = []
    while(iterator!=len(array)):
        temp = array[i]
        if temp not in newList:
            newList.append(temp)
        iterator += 1
    return newList
