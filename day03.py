# sub = {"python" : "kim", "c++" : "sung", "datastructure" : "kim","database" : "kang"}
# sub2 = {"python" : "kim", "c++" : "sung", "datastructure" : "kim","database" : "kang"}
# print("{0[python]}, {1[datastructure]}".format(sub,sub2))

#prime number(솟수)
number = int(input("Input number : "))
count = 0
i = 2
while i<number:
    if number%i == 0:
        count += 1
        break
    i += 1
if count == 0:
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")