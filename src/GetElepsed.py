from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import datetime

class GetElepsed(object):

    # startからendまでのElapsedを返す
    @staticmethod
    def getElepsed(start, end) :
        try :
            return (end - start).total_seconds()
        except Exception as e :
            print(e)

    # startからnowまでのElapsedを返す
    @staticmethod
    def getElepsedNow(start) :
        try :
            now = datetime.datetime.now()
            return GetElepsed.getElepsed(start, now)
        except Exception as e :
            print(e)
    
    
