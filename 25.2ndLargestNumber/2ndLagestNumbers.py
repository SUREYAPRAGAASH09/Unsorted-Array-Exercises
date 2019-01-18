import Max

def secondLargestNumber(array):
    v = Max.Max(array)
    for i in array:
        if v == i:
            array.remove(i)
    maxi = Max.Max(array)
    
    return maxi

array = [3,1,6,9,3]
print(secondLargestNumber(array)) 