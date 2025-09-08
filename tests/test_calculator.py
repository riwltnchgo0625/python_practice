# tests/test_calculator.py
import pytest

#from apps.calculator import Calculator
# 픽스쳐(fixture)
# @pytest.fixture
# def calcurator_instance():
#     c = Calculator()
#     return c

def test_add(calcurator_instance):
    assert calcurator_instance.add(3,4) == 7
    assert calcurator_instance.add(-2,-4) == -6

def test_sub(calcurator_instance):
    assert calcurator_instance.sub(10,4) == 6

def test_div(calcurator_instance):
    assert calcurator_instance.div(8,4) == 2
    assert calcurator_instance.div(1,3) == pytest.approx(1/3)
    with pytest.raises(ZeroDivisionError):
        calcurator_instance.div(3,0)
        