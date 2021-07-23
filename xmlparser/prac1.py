# 폴더에 파일 리스트 불러오기
# os 모듈에 listdir 메소드 사용하면 됨
# os.listdir("dir path") => 파일 리스트로 구성된 list 객체 반환
# embedded null character in path = 경로에 널 문자가 포함 되어있음
# 원인은 '\0' 이게 널포인트문자이기 때문
# 해결 방법은 문자열 앞에 r 포메팅을 해주면 됨
# '\' 이걸 '/' 이걸루 바꿔줘두 됨
import os
dir = os.listdir(r'\\10.21.10.204\fab 기술\fab기술\00_BackPart\06_심영현\설비별 알람 리스트\log_file\28W')

print(dir)