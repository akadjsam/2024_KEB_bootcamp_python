def test(f):
    """
    decorator 함수 시작하면 start 출력, 함수 끝나면 end 출력
    :param f: function
    :return: closure function
    """
    #def test_in():
    def test_in(*args,**kwargs):
        print('start')
        #f() 이렇게 하면 리턴 생략 가능
        result = f(*args,**kwargs)
        print('end')
        return result
    return test_in
@test
def greeting():
    print("안녕하세요")

greeting()