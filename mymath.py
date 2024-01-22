#prime number(솟수)

if __name__ == "__main__":
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

    def fahrenheit_to_celsius(fahrenheit):
        return float((fahrenheit - 32.0) * 5.0 / 9.0)
    def celsius_to_fahrenheit(celsius):
        return float((celsius * 9.0/5.0) + 32.0)

else:
    print("mymath is not a main file")