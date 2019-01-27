# Given an unsorted integer array A and an integer value X, find if X is found more than once in A.
#input = array 
#output = if more than one element is found return true else false

def count(a):
    counti = 0
    while(a[counti:]):
        counti += 1

    return counti

def find_more_than_once(array,search_elemnt):
    flag = False
    i = 0
    b = count(array)
    counti = 0
    while (i!=b):
        if (array[i] == search_elemnt):
            counti += 1
        i += 1
    if counti == 2:
        flag = True
    return flag

        
    
search_elemnt = 2
print("---------------------------------------------")
array = [7,9,1,2,4]
print(find_more_than_once(array,search_elemnt))
print("---------------------------------------------")
