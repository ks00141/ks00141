# xml Dir file list에 확장자 .xml말고 다른 확장자가 있는지 확인하는 프로그램

import os

tool_num = None
week = None
start_date = None
end_date = None
date = None

tool_num, week = input('tool num : '),input('week : ')


path = f'//10.21.10.204/fab 기술/fab기술/00_BackPart/06_심영현/설비별 알람 리스트/log_file/{week}w/#{tool_num}'

# try : 일단 실행해서 오류가 발생하면 except문으로 분기
# except : try문에서 실행된 결과가 오류이면 실행
# else : 오루가 발생 하지 않았을때 실행
# finally : 오류 발생 유무와 상관없이 항상 실행
try:
    files = os.listdir(path)
except:
    print("empty dir or dir path error")
else:
    start_date = input('start_date : ')
    end_date = input('end date : ')
    date = list(range(int(start_date),int(end_date)+1))    
    for day in date:
        try:
            os.listdir(f'{path}/{day}')
        except:
            print("invalid date")

        else:
            dest_path = None
            dest_path = path + f'/{day}'
            xml_files = os.listdir(dest_path)
            print(f'-------{day}-------')   
            print(f'Count : {len(xml_files)}')
