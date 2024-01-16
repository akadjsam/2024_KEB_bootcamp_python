#예외처리 preview
sub = "python c++ database linux"
print("%e"%0.703)
print(sub.isalnum()) # 공백, +가 있기때문에 false, 오직 알파벳 혹은 숫자로 이루어져 있어야 한다.
sub_input = input("수강신청과목 입력 : ")
try:
    print(f'해당 과목은 존재합니다. 위치는 {sub.index(sub_input)}번 인덱스입니다.') #sub.find(sub_input)로 대체 가능.
except ValueError:
    print("해당과목이 존재하지 않습니다.")

