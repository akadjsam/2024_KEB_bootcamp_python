#prime number(솟수)
numbers = input("Input First number and Second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])
if n1 > n2:
    n1, n2 = n2, n1
for number in range(n1,n2+1):
    isPrime = True
    if number < 2:
        pass
    else:
        for i in range(2,number):
            if number%i == 0:
                isPrime = False
                break
        if isPrime:
            print(number, end=' ')