#14. Given an unsorted integer array A, print the contents of the array in the 
# given format: {arrayindex:value, arrayindex:value}. 
# Note that there is no comma after the last value.

import Finding_lenght_of_an_array_without_using_len_functin
def printing_index_with_values(array):
    dictionary = {}
    index = 0
    lenght = Finding_lenght_of_an_array_without_using_len_functin.count(array)
    while(index!=lenght):
        dictionary[index] = array[index]
        index += 1
    return dictionary

array = [9,7,3,4,0]
print(printing_index_with_values(array))