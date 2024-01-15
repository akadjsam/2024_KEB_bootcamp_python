# money = 5,000,000
# print(money) #In python -> tuple
# print(type(money))
#
# cash = 5_000_000
# print(cash)
# print(type(cash)) #int

base_number = int(input('Input base number : '))
exponent_number = int(input('Input exponent number : '))
# f-string
# print(f'base is {base_number}, exponent is {exponent_number}, result is {base_number ** exponent_number}') p.79
print(f'base is {base_number}, exponent is {exponent_number}, result is {pow(base_number, exponent_number)}')

#format
print("base is {0}, exponent is {1}, result is {2}".format(base_number, exponent_number, pow(base_number, exponent_number)))
print("base is {}, exponent is {}, result is {}".format(base_number, exponent_number, pow(base_number, exponent_number)))

# c like
print("base is %d, exponent is %d, result is %d" %(base_number, exponent_number, pow(base_number, exponent_number)))

