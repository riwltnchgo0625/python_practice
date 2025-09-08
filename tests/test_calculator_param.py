# tests / test_calculator_param.py


import pytest

add_test_cases=[
    (2,3,5),
    (-1,-1,-2),
    (5,-3,2),
    (-5,3,-2),
    (0,0,0),
    (0.1, 0.2, pytest.approx(0.3)),
    (100000000, 200000000,300000000),
    pytest.param(100000000, 200000000,300000000, id="large numbers")
]
@pytest.mark.parametrize("a, b, expected", add_test_cases)
def test_add_cases(calcurator_instance, a, b, expected):
    assert calcurator_instance.add(a,b) == expected

# 예외테스트 파라미터화 
div_test_cases=[
    (10, 0, ZeroDivisionError),
    ("10", 2, TypeError),
    (10,"2", TypeError),
    (None, 2, TypeError)
]
@pytest.mark.parametrize("a,b,expected", div_test_cases)
def test_div_exceptions(calcurator_instance, a, b, expected):
    with pytest.raises(expected):
        calcurator_instance.div(a,b)

@pytest.mark.parametrize("x", [1,2])
@pytest.mark.parametrize("y",[10,100])
def test_multiparam_cases(x,y):
    assert isinstance(x, int)
    assert isinstance(y, int)