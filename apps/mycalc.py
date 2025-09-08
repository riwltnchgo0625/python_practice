
def add(a, b):
    if not isinstance(a,(int, float)) or not isinstance(b,(int,float)):
        raise TypeError("숫자만 입력하세요")
    return a+b

def sub(a, b):
    if not isinstance(a,(int, float)) or not isinstance(b,(int,float)):
        raise TypeError("숫자만 입력하세요")
    return a-b

def div(a, b):
    if not isinstance(a,(int, float)) or not isinstance(b,(int,float)):
        raise TypeError("숫자만 입력하세요")
    if b == 0 :
        raise ZeroDivisionError("0으로 나눌수 없습니다")
    return a/b

