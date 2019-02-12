#Test File for Comparing Two Element in an Unsorted Integer Array

import Compare_Two_Array_Elements

def assertTrue(): # Environment Test
    assert True

def test_array1_array2retutnFalse():
    #arrange
    array1 = [2,8,1,4,5]
    array2 = [2,9,1,4,5]
    excepted = False
    #act
    actual = Compare_Two_Array_Elements.compareArrayElements(array1,array2)
    #assert
    assert excepted == actual


def test_array1_array2retutnTrue():
    #arrange
    array1 = [2,9,1,4,5]
    array2 = [2,9,1,4,5]
    excepted = True
    #act
    actual = Compare_Two_Array_Elements.compareArrayElements(array1,array2)
    #assert
    assert excepted == actual


def test_array1_array2retutn1False():
    #arrange
    array1 = [2,9,1,4,5,]
    array2 = [2,9,1,4,5]
    excepted = True
    #act
    actual = Compare_Two_Array_Elements.compareArrayElements(array1,array2)
    #assert
    assert excepted == actual
