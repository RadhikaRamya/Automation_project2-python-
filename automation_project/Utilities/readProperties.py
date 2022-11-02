import configparser

config1 = configparser.RawConfigParser()
config1.read("C:\\Users\\Harsha\\Desktop\\automation_project\\Configurations\\config.ini")


class ReadConfig1:
    @staticmethod
    def getApplicationURL():
        url = config1.get('common info', 'baseURL')
        return url

    @staticmethod
    def getusername():
        username1 = config1.get('common info', 'username')
        return username1

    @staticmethod
    def password():
        password1 = config1.get('common info', 'password')
        return password1

    @staticmethod
    def getApplicationURL1():
        url1 = config1.get('basic info', 'baseURL1')
        return url1

    @staticmethod
    def getusername1():
        username2 = config1.get('basic info', 'usr')
        return username2

    @staticmethod
    def password1():
        password2 = config1.get('basic info', 'psswrd')
        return password2

    @staticmethod
    def personalURL():
        URL3 = config1.get('employ info', 'baseURL2')
        return URL3

