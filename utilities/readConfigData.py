import configparser

parser = configparser.RawConfigParser()
parser.read(".\\configuration\\configData.ini")

class ReadConfig:
    @staticmethod
    def getBaseURL():
        url = parser.get("commonData","base_url")
        return url

    @staticmethod
    def getUserName():
        name = parser.get("commonData","userName")
        return name

    @staticmethod
    def getCommonData(row_Key,key_value):
        value = parser.get(row_Key,key_value)
        return value


