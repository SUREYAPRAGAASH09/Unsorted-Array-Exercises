def remove_Dupli(array):
    i = 0
    b = []
    while(i!=len(array)):
        temp = array[i]
        if temp not in b:
            b.append(temp)
        i += 1
    return b 
array = [7,1,2,4,8,9,7]
print(remove_Dupli(array))