from GetElepsed import GetElepsed

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import datetime

class Sample(object):
    
    # driverpath=各種Webドライバーexeのフルパス
    def __init__(self, driverpath):
        # ドライバーパスを指定 
        self.driver = webdriver.Chrome(driverpath)
        # URLに移動
        self.driver.get("http://natto0wtr.web.fc2.com/CookieClicker/")

    def isOverLimitTime(self, start ,limitTime) :
        try :
            return GetElepsed.getElepsedNow(start) > limitTime
        except Exception as e :            
            print(e)

    # フォルダ作ってスクショ
    def screenshot(self):
        try:
            p = Path('./images/' + self.__class__.__name__  + '/')
            p.mkdir(parents=True, exist_ok=True)
            
            now = datetime.datetime.now()
            imgpath = str(p.resolve()) + "\\" + now.strftime("%Y%m%d%H%M%S%f") + "_last.png"

            self.driver.get_screenshot_as_file(imgpath)
        except Exception as e :
            print(e)

    def clickBigCookie(self) :
        # cookieボタン見つけてクリックさせる
        try :
            element = self.driver.find_element_by_id("bigCookie")
            element.click()
        except Exception as e :
            print(e)
    def getBeforeExecFunctions(self) :
        self.beforeExecFunctions = []
    def getBeforeDoExecFunctions(self) :
        self.beforeDoExecFunctions = []
    def getDoExecFunctions(self):
        self.doExecFunctions = []
        self.doExecFunctions.append(self.clickBigCookie)        
    def getAfterDoExecFunctions(self) :
        self.afterDoExecFunctions = []
    def getAfterExecFunctions(self) :
        self.afterExecFunctions = []        

    #　各メソッド埋め込む処理
    # 開始終了以外は継承先で介入できるように適当に
    def init(self):
        self.getBeforeExecFunctions()
        self.getBeforeDoExecFunctions()
        self.getDoExecFunctions()
        self.getAfterDoExecFunctions()
        self.getAfterExecFunctions()

    def beforeExec(self):
        for func in self.beforeExecFunctions:
            try :
                func()
            except Exception as e :
                print(e)               

    def afterExec(self):
        for func in self.afterExecFunctions :
            try :
                func()
            except Exception as e :                    
                print(e)

    def beforeDoExec(self):
        for func in self.beforeDoExecFunctions :
            try :
                func()
            except Exception as e :                    
                print(e)

    def doExec(self) :
        for func in self.doExecFunctions:
            try :
                func()
            except Exception as e :                    
                print(e)
    def afterDoExec(self):
        for func in self.afterDoExecFunctions:
            try :
                func()
            except Exception as e :                    
                print(e)
            
    # limitTime:指定時間を超えたら止める.
    def exec(self, limitTime):
        self.init()

        #計測開始（開始時間も経過で処理する場合もあるから定義）
        self.start = datetime.datetime.now()

        # 前処理
        # ---ここから介入---
        self.beforeExec()
        while (not self.isOverLimitTime(self.start, limitTime)) :
            try :
                self.beforeDoExec()
                self.doExec()
                self.afterDoExec()
            except Exception as e :
                print(e)
        # 後処理
        self.afterExec()
        # ---ここまで介入---

        #スクショ取っておく
        self.screenshot()
        #終了
        self.driver.quit()
