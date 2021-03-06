#36. Given an unsorted integer array A containing 
# elements from 0-9, find the number of not unique elements.
import find_min
import dictionaryOperations
def findUnique(array):
    not_unique = []
    dictionary = dictionaryOperations.built_dictionary(array)
    listValues = list(dictionary.values())
    minimum_value = find_min.findMin(listValues)
    for i in listValues:
        if i != minimum_value :
            b = (dictionaryOperations.find_key_from_dictionary(dictionary,i))
            not_unique.append(b)
            dictionary.pop(b)
    return not_unique
print("================================")
array = [5,7,8,2,6,5,8]
print(findUnique(array))
#print(built_dictionary(array)) 
print("================================")