sub = "python c++ database linux"
sub_input = input("수강신청과목 입력 : ")
if sub.find(sub_input) != -1:
    print(f'해당 과목은 존재합니다. 위치는 {sub.index(sub_input)}번 인덱스입니다.') #sub.find(sub_input)로 대체 가능.
else:
    print("해당과목이 존재하지 않습니다.")