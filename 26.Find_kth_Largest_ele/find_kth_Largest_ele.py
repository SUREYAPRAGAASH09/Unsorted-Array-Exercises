import Max
import FindLenght
import find_min
def kth_largest_ele(array,kthele):
    lenght = FindLenght.count(array)
    if (lenght == kthele):
        return find_min.findMin(array)
    else:

        iterator = 1
        while(iterator!=kthele):
            Largest_ele = Max.Max(array)
            for j in array:
                if (j == Largest_ele):
                    array.remove(Largest_ele)
            iterator += 1
        Largest_ele = Max.Max(array)
    return Largest_ele
print("========================") 

array = [5,1,9,7,2,8,3,6,4]
kthele = 1
#print()
v = kth_largest_ele(array,kthele)
print("The {0} Largest Element in the array is {1}".format(kthele,v))
print("==================================================================")