import configparser

config = configparser.ConfigParser()

config.read('config.ini','w')

config.write("[test]")