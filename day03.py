#prime number(솟수)
number = int(input("Input number : "))
isPrime = True
if number < 2:
    print(f"{number} is not prime number")
else:
    for i in range(2,number):
        if number%i == 0:
            isPrime = False
            break


if isPrime: #remove count == 0
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")