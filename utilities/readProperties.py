import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class Readconfig:

    @staticmethod
    def getApplicationURL():
        url=config.get('commonInfo','baseURL')
        return url

    @staticmethod
    def getUseremail():
        useremail=config.get('commonInfo','email')
        return useremail

    @staticmethod
    def getPassword():
        password=config.get('commonInfo','password')
        return password
    