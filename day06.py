import random as ra
class OopsExaception(Exception):
    pass

# numbers = []
# for i in range(10):
#     numbers.append(ra.randint(1,100))
numbers = [ra.randint(1,100) for i in range(10)]
print(numbers)
try:
    pick = int(input(f"Input index (0 ~ {len(numbers)-1}): "))
    print(numbers[pick])
    print(5/2)
    raise OopsExaception("Oops") #코드에 에러가 없어도 에러를 발생시킴("Oops")라는 에러를 출력
except IndexError as e:
    print("error : ",e)
except ValueError as e:
    print("error : ", e)
except ZeroDivisionError as e:
    print("error : ",e)
except Exception as e: #문법상 except 중 맨 아래에 위치해야 한다.
    print("error occurs :", e)
else:
    print("Program Terminate")