try:
    f = open("output.txt","w")
except Exception as e:
    print("예외가 발생했습니다", e)
else:
    print("파일오픈성공")
    f.close()

def div(a,b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없어요")
    return a/b

div(3,0)

