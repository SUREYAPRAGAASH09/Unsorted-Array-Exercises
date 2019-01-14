import Find_More_than_once

def test_assertTrue():
    assert True

def test_array_return_False():
    #arrange
    search_elemnt = 2
    array = [7,9,1,2,4]
    excepted = False
    #act
    actual = Find_More_than_once.find_more_than_once(array,search_elemnt)
    #assert
    assert excepted == actual