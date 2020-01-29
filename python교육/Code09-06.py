def func1():
    a = 10  # 지역변수
    print("func1()에서 a값 %d" % a)


def func2():
    print("func2()에서 a값 %d" % a)


# 전역변수선언부분
a = 20  # 전역변수

func1()
func2()
