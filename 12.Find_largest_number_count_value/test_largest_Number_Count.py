import find_largest_number_count
def assertTrue():
    assert True 

def arrayreturn2():
    #arrange
    array = [3,9,2,7,9]
    excepted = 2
    #act
    actual = find_largest_number_count.find_largest_numbers_occurences(array)
    #assert
    assert excepted == actual
    