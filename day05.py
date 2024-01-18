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

while True:
    menu = input("1) Fahrenheit to Celsius\t2) Celsius to Fahrenheit\t\
    3) Check Prime Number\t4) Specify the Prime Number's range(2 inputs)\t5) Quit program : ")

    #Fahrenheit to Celsius
    if menu == '1':
        fahrenheit = float(input("Input Fahrenheit : "))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')

    # Celsius to Fahrenheit
    elif menu =='2':
        Celsius = float(input("Input Fahrenheit : "))
        print(f'CelsiusQD : {Celsius}C, Fahrenheit : {((Celsius * 9.0/5.0) + 32.0):.4f}F')

    # Check Prime Number
    elif menu == '3':
        number = int(input("Input number : "))
        if isPrime(number):
            print(f"{number} is prime number")
        else:
            print(f"{number} is not prime number")
        print()

    # Specify range
    elif menu == '4':
        prime_list = []
        n1, n2 = map(int, input("Input First number and Second number : ").split())
        n1, n2 = min(n1, n2),max(n1,n2) #패킹
        # numbers = input("Input First number and Second number : ").split()
        # n1 = int(numbers[0])
        # n2 = int(numbers[1])
        # if n1 > n2:
        #     n1, n2 = n2, n1
        for number in range(n1, n2 + 1):
            if isPrime(number):
                prime_list.append(str(number)) # number(int)를 string으로 변환하여 리스트에 추가

        prime_str = ", ".join(prime_list) # join으로 list를 string으로 변환

        if len(prime_list) == 0:
            print(f'{n1}와 {n2} 사이의 소수가 존재하지 않습니다.')
        else:
            print(f'{n1}와 {n2} 사이의 소수는 {prime_str} 입니다.')
        print()

    # Quit program
    elif menu == '5':
        print("Terminate program")
        break
    else:
        print("choose number 1 or 2 or 3!")
