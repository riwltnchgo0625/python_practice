# apps/calcurator.py  class 기반

class Calculator:
    def add(self, a, b):
        if not isinstance(a,(int, float)) or not isinstance(b,(int,float)):
            raise TypeError("숫자만 입력하세요")
        return a+b

    def sub(self,a, b):
        if not isinstance(a,(int, float)) or not isinstance(b,(int,float)):
            raise TypeError("숫자만 입력하세요")
        return a-b

    def div(self,a, b):
        if not isinstance(a,(int, float)) or not isinstance(b,(int,float)):
            raise TypeError("숫자만 입력하세요")
        if b == 0 :
            raise ZeroDivisionError("0으로 나눌수 없습니다")
        return a/b