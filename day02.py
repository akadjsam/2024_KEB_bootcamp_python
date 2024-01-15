# first_number = int(input("First Number : "))
# second_number = int(input("Second Number : ")) #p.83
#
# quotient = first_number // second_number
# remainder = first_number % second_number
#
# print(f'quotient : {quotient}, remainder : {remainder}')

first_number = int(input("First Number : "))
second_number = int(input("Second Number : ")) #p.83

print(f'quotient : {divmod(first_number,second_number)[0]}, remainder : {divmod(first_number,second_number)[1]}')
