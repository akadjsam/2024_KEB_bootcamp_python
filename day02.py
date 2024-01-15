letter = input("Input alphabet letter : ")

#vowels = {'a','e','i','o','u'} #set
vowels = "aeiou" #string
if letter in vowels:
    print(f'q{letter} is a vowle')
else:
    print(f'{letter} is a consonant')