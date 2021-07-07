import configparser

config = configparser.ConfigParser()
config.read("config.ini")

print(f'설정 전{config["USERSET"]["ID"]}')
config["USERSET"]["ID"] = "ks00141"
with open("./config.ini","w") as configfile:
    config.write(configfile)
print(f'설정 후{config["USERSET"]["ID"]}')