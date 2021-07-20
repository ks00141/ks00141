
# open() <- Logical File Chanel을 생성하기 위한 Method (FD / File Descripter)
# 인자로는 ("File Path","Mode","Encoding /생략하면 UTF-8로 기본설정)
f = open("./pracfolder/test1.ini","w")

# FD.write method를 이용하여 파일 쓰기
f.write("[test]\n")
f.write("title=test\n")
f.write("desc=FileIOTest")

# 파일 연산을 완료 하고나서는 항상 닫아줘야 한다 !

f.close()