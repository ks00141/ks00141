# xml 파일 열어서 원하는 태그내용만 가져오기
# xml을 객체화하기 위해서 xml.etree.ElementTree를 import 해준다
import os
import xml.etree.ElementTree as etree

# 파일열때 경로를 동적으로 사용하기 위해 변수에 저장
path = f'//10.21.10.204/fab 기술/fab기술/00_BackPart/06_심영현/설비별 알람 리스트/log_file/{28}w/#{9}/{12}'
files = os.listdir(path)

# xml파일로부터 xml객체화를 하는경우
# xml.etree.ElementTree.parser('file path') method를 사용한다
for file in files:
    parser_file = etree.parse(f'{path}/{file}')
        
    # xml파일을 객체로 파싱후 xml객체의 method중 find를 사용하여 내가 원하는 태그를 반환 받을수 있다
    xml_desc = parser_file.find('/Description')
    xml_time = parser_file.find('/TimeStamp')
    print(f'Time : {xml_time.text}, desc : {xml_desc.text}')