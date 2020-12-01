import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class Readconfig():
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUserName():
        Username=config.get('common info','Username')
        return Username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password