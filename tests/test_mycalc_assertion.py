# test_mycalc_assertion.py

import pytest
from apps.mycalc import add, sub, div

def test_various_assertion():
    # 참거짓 검증 
    assert True
    assert 0 == False
    assert 1 == True
    assert not ""
    assert not []

    # 비교검증
    assert  5 > 3
    assert  7 != 8

    # 멤버 연산자
    assert 'a' in 'apple'
    assert 5 not in [1,2,3]

    #동일성 검증 
    a = [1,2]
    b = [1,2]
    c = a
    assert a == b
    assert a is not b
    assert a is c

def test_div_float():
    result = div(1,3)
    assert result == pytest.approx(1/3)
    assert div(10,2) == pytest.approx(5.0)    

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(3,0)

def test_wrong_type():
    with pytest.raises(TypeError):
        add(3,"4")

import warnings
def function_that_warns():
    warnings.warn("이 함수는 곧 제거될 예정입니다.", DeprecationWarning)
    return True

def test_warning():
    with pytest.warns(DeprecationWarning):
        assert function_that_warns()