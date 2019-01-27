 # To find the min of dictionary values 
import FindLenght
def find_smallest_value(values):

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
print("---------------------------------------------")
#values = [5,2,4,7,2,5]
#print(find_smallest_value(values))
print("---------------------------------------------")