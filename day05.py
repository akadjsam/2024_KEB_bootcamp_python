#prime number(솟수)

def isPrime(n) -> bool: # -> bool 은 리턴타입이 무엇인지 알려주는 역할, 안써도 상관은 없다.
    """
    매개변수로 넘겨 받은 수가 소수 여부를 boolean type으로 리턴한다
    :param n: 판정할 매개변수
    :return: 소수이면 true, 아니면 false return. 
    """ #가이드라인 help(isPrime)
    if n < 2:
        return False
    else:
        i = 2
        while i**2 <= n:
            if n%i == 0:
                return False
            i += 1
        return True

numbers = input("Input First number and Second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])
if n1 > n2:
    n1, n2 = n2, n1
for number in range(n1,n2+1):
    if isPrime(number):
        print(number, end=' ')


