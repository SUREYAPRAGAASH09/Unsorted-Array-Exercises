#3. Given an unsorted integer array A and an integer value X,
#  return the index at which X is located in A or return -1 if it is not found in A.
#import FindLenght
def getIndex(array,indexFor):
    index = 0
    i = 0
    lennght = len(array)
    while (i!=lennght):
        if (array[i] == indexFor):
            break
        index += 1
        i += 1
    return index
print("-----------------------------------------")
array = [7,4,5,7]
indexFor = 5
print(getIndex(array,indexFor))
print("---------------------------------------------")