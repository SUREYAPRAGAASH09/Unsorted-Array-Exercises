Question :
==========
 Given an unsorted integer array A, print the contents of the array in the  given format: {arrayindex:value, arrayindex:value}. 
Note that there is no comma after the last value.
Input :
=======
    Unsorted Array 
Output :
========
    print the contents of the array in the  given format: {arrayindex:value, arrayindex:value}
    
Algorithm :
===========
    Using Dictionary Data structure insert the all the arraya elemnts into the Dictionary and print dictionary 
     
import Findlenght
def Printarraywithindexer(array):
    dictionary = {}
    index = 0
    lenght = Finding_lenght_of_an_array_without_using_len_functin.count(array)
    while(index!=lenght):
        dictionary[index] = array[index]
        index += 1
    return dictionary

