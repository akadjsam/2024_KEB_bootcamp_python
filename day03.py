# course = "2024 KEB Bootcamp"
# print(course)
# list_course = course.split() #아무것도 입력하지 않으면 스페이스 기준으로 리스트에 담기
# list_course = course.split('B') # 출력 결과 : ['2024 KE', ' ', 'ootcamp'] B를 구분기호로 지정
# print(list_course)

# split : string to list
# join : list to string

# num = input("First number Second number").split()
# print(type(num)) #num's type is 'list'
# # print(num[0]+num[1]) #concatenation
# print(int(num[0])+int(num[1])) #arithmetic opeartion

sub = ["python", "c++", "database"]
sub = "/ ".join(sub)
print(sub)