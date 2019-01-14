# Given an unsorted integer array A and an integer value X, find if X is found more than once in A.
#input = array 
#output = if more than one element is found return true else false

# Given an unsorted integer array A and an integer value X, find if X is found more than once in A.
#input = array 
#output = if more than one element is found return true else false

def count(a):
    counti = 0
    while(a[counti:]):
        counti += 1

    return counti

def find_more_than_once(array,search_elemnt):
    
    i = 0
    b = count(array)
    counti = 0
    while (i!=b):
        if (array[i] == search_elemnt):
            counti += 1
        i += 1
    
    return counti

        
    
search_elemnt = 4
array = [7,2,1,2,4]
count = find_more_than_once(array,search_elemnt)
print("The Number {} occurs {} times".format(search_elemnt,count))
