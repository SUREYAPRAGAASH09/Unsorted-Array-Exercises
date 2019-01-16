 # To find the max of dictionary values 
import FindLenght
def max(values):

    values_count = FindLenght.count(values) 
    one = values[0] 
    two = values[1] 
    if (one > two): 
        max = one 
    else: 
        max = two 
    i = 2 
    while(i!=values_count): 
        if (values[i]>max): 
            max = values[i] 
        i += 1 
    return max 

#values = [5,2,4,7,3,5]
#print(find_largest_value(values))