#(32°F − 32) × 5/9 = 0°C

#(0°C × 9/5) + 32 = 32°F
temp = []
if temp:
    print("full") #temp = [0]
else:
    print("empty")

menu = input("1) Fahrenheit to Celsius\n2) Celsius to Fahrenheit\n3) Quit program\n")

if menu == '1':
    fahrenheit = float(input("Input Fahrenheit : "))
    print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')

elif menu =='2':
    Celsius = float(input("Input Fahrenheit : "))
    print(f'Celsius : {Celsius}C, Fahrenheit : {((Celsius * 9.0/5.0) + 32.0):.4f}F')
else:
    print("Terminate program")