# 입력받아서 특정 파일 경로 리스트 출력하기
# log파일 구조는 
# root(설비별 알람 리스트)
#  └ result
#    log_file
#    └ #9
#      #10
#      #11
#      #12
#       └ (일자별로 명명된 폴더 / ex : 12)
#           └ xml files

import os

# 필요한 변수
#  1) Tool
#  2) 조회 일자
#  3) 조회 주차

tool_num = None
date = None
week = None

# tool_num = input('tool num ? :')
# week = input('week ? : ')
# date = input('date ? : ')

tool_num = 9
week = 28
date = 12

files = os.listdir(f'//10.21.10.204/fab 기술/fab기술/00_BackPart/06_심영현/설비별 알람 리스트/log_file/{week}w/#{tool_num}/{date}')
path = f'//10.21.10.204/fab 기술/fab기술/00_BackPart/06_심영현/설비별 알람 리스트/log_file/{week}w/#{tool_num}/{date}'

file = files[0]

open_file = open(f'{path}/{file}','r')

print(open_file.read(3000))