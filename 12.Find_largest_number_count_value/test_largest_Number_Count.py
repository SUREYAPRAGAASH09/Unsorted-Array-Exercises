#Test File for finding the Counting Occruence of largest Number in an Unsorted Integer Array  
import find_largest_number_count
def assertTrue(): #Environment Test
    assert True 

def arrayreturn2(): #Counting Occurence of Largest Number Test 
    #arrange
    array = [3,9,2,7,9]
    excepted = 2
    #act
    actual = find_largest_number_count.find_largest_numbers_occurences(array)
    #assert
    assert excepted == actual
    
