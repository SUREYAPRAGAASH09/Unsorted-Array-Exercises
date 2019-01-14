#6. Given an unsorted integer array A and 
#an integer value X, return the indices of the locations where X is found in A.

def getIndex(array,indexFor):
    index_list = []
    i = 0
    index = 0
    lennght = len(array)
    while (i!=lennght):
        if (array[i] == indexFor):
            index_list.append(index)
        index += 1
        i += 1
    return index_list

array = [7,4,5,7]
indexFor = 7
print(getIndex(array,indexFor))