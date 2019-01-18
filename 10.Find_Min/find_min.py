 # To find the min of dictionary values 
import FindLenght
def findMin(values):

    values_count = FindLenght.count(values) 
    one = values[0] 
    two = values[1] 
    if (one < two): 
        min = one 
    else: 
        min = two 
    i = 2 
    while(i!=values_count): 
        if (values[i]<min): 
            min = values[i] 
        i += 1 
    return min 

#values = [5,0,1,7,3,5]
#print(findMin(values))