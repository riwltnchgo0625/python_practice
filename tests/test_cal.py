from apps.calculator import Calculator
import pytest

class TestCalculator:
    #setup_method() 각 테스트 함수 실행 전 실행됨
    def setup_method(self):
        # 각 테스트 전에 실행
        self.calc = Calculator()

    def test_add(self):
        assert self.calc.add(2, 3) == 5

    def test_div(self):
        assert self.calc.div(10, 2) == 5.0

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(10, 0)