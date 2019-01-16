import find_min
def test_AssertTrue():
    assert True

def test_arrayretutn7():
    #arrange
    values = [5,2,4,7,3,5]
    excepted = 2
    #act
    actual = find_min.findMin(values)
    #assert
    assert excepted == actual 