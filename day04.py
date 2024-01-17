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
        i = 2
        while i*i < number: #제곱을 활용하여 반복문 횟수 줄임 -> 성능개선
            if number%i == 0:
                isPrime = False
                break
            i += 1
            #print(i,end=' ') #loop count
        if isPrime:
            print(number, end=' ')