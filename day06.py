def fac1(n):
    """
    반복문을 이용한 팩토리얼 함수
    :param n: int
    :return: factorial(int)
    """
    result = 1
    for i in range(2,n+1):
        result = result * i
    return result

def factorial_recursion(n):
    """
    재귀함수를 이용한 재귀함수ㅡ
    :param n: int
    :return: function(int)
    """
    if n == 1:
        return n
    elif n <=0:
        print("error : ",end='')
        return n
    else:
        return n * factorial_recursion(n-1)

print(fac1(5))
print(factorial_recursion(-1))