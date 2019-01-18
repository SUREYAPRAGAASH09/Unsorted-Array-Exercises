import removeDuplicates

def test_assertTrue():
    assert True

def test_array_return_list():
    #arrange
    array = [7,2,0,1,5,7,9,1,8]
    excepted = [7, 2, 0, 1, 5, 9, 8]
    #act
    actual = removeDuplicates.built_dictionary(array)
    #assert
    assert excepted == actual
