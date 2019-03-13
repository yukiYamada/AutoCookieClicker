from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import datetime

class Sample:
    
    # driverpath=各種Webドライバーexeのフルパス
    def __init__(self, driverpath):
        # ドライバーパスを指定 
        self.driver = webdriver.Chrome(driverpath)
    def isOverLimitTime(self, start ,limitTime) :
        try :
            now = datetime.datetime.now()

            return (now - start).total_seconds() > ((start + datetime.timedelta(seconds=limitTime)) - start).total_seconds()

        except Exception as e :            
            print("isOverLimitTime:" + e)

    # フォルダ作ってスクショ
    def screenshot(self):
        try:
            p = Path('./images/' + self.__class__.__name__  + '/')
            p.mkdir(parents=True, exist_ok=True)
            
            now = datetime.datetime.now()
            imgpath = str(p.resolve()) + "\\" + now.strftime("%Y%m%d%H%M%S%f") + "_last.png"

            self.driver.get_screenshot_as_file(imgpath)
        except Exception as e :
            print("screenshot:" + e)
            
    # limitTime:指定時間を超えたら止める.
    def exec(self, limitTime):
        # URLに移動
        self.driver.get("http://natto0wtr.web.fc2.com/CookieClicker/")

        #計測開始
        start = datetime.datetime.now()
        while (not self.isOverLimitTime(start, limitTime)) :
            try :
                # cookieボタン見つけてクリックさせる
                element = self.driver.find_element_by_id("bigCookie")
                element.click()

            except Exception as e :
                print(e)
        
        #スクショ取っておく
        self.screenshot()

        #しゅうーりょうー
        self.driver.quit()
