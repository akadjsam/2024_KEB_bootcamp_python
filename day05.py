# def my_range(first=0,last=10,step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step
#
# r = my_range()
# print(r,type(r))
# for i in r:
#     print(i)
#
# for i in r: #이 반복문은 실행되지 않음
#     print(i)

def deco(func):
    def new_func(a):
        print(func.__doc__)
        result = func(a)
        return result
    return new_func
@deco
def squares(n):
    """
    제곱근
    :param n: int
    :return: int
    """
    return n*n

print(squares(5))