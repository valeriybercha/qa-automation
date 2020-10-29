import configparser

# Configuring data from the 'config.ini' file

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getApplicationUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getApplicationPassword():
        password = config.get('common info', 'password')
        return password

