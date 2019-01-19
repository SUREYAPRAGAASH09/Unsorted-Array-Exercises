import find_min

def secondsmallestNumber(array):
    v = find_min.findMin(array)
    for i in array:
        if v == i:
            array.remove(i)
    maxi = find_min.findMin(array)
    
    return maxi

array = [3,1,6,9,3]
print(secondsmallestNumber(array)) 