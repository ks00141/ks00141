import configparser
config = configparser.ConfigParser()


config.read('ROW_STRINg.ini',encoding='utf-8')

print(config.sections()[0])