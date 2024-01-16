# course = "2024 KEB Bootcamp"
# print(course.replace('KEB', 'INHA'))
# print(course) #output : 2024 KEB Bootcamp (immutable)
# course = course.replace('KEB', 'INHA')
# print(course)

# course = "KEB 2024 KEB Bootcamp"
# course = course.replace('KEB', 'INHA',2) #3번째 인수는 변경할 숫자를 의미함.
# print(course)

# course = "*KEB 2024# KEB !Bootcamp...*!#"
# course = course.strip("!#.*") #연속적으로 되어 있는 것들만 삭제(끝에 있는 것들)
# print(course)

course = "* KEB 2024# KEB !Bootcamp KEB...*!#"
print(course.find('KEB'))
print(course.rfind('KEB')) #reverse
print(course.index('KEB'))
print(course.rindex('KEB')) #reverse
print(course.find('inha')) # -1 return
# print(course.index('inha')) # value error