import pytest
#import apps.mycalc 
from apps.mycalc import add,sub

def test_add_positive_num():
    # 준비 
    a = 3
    b = 4
    expected_result = 7
    
    # 실행
    actual_result = add(3,4)

    #검증
    assert actual_result == expected_result

def test_add_negative_num():
    assert add(-2,-4) == -6

def test_sub_positive_num():
    assert sub(2,4) == -2

def test_sub_negative_num():
    assert sub(-2,-4) == 2