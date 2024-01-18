def squares(*n) -> list:
    """
    넘겨 받은 수치 데이터들의 제곱값을 리스트에 담아서 확인
    :param n: tuple
    :return: list
    """
    return [i*i for i in n]
def run_function(f, *number1) -> list:
    return f(*number1)
print(squares(7,5,2))
print(run_function(squares,9,10))