
import Max

def test_AssertTrue():
    assert True

def test_arrayretutn7():
    #arrange
    values = [5,2,4,7,3,5]
    excepted = 7
    #act
    actual = Max.Max(values)
    #assert
    assert excepted == actual