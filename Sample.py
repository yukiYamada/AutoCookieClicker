from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Sample:
    
    # driverpath=各種Webドライバーexeのフルパス
    def __init__(self, driverpath):
        # ドライバーパスを指定 
        self.driver = webdriver.Chrome(driverpath)

    def exec(self):
        # URLに移動
        self.driver.get("http://natto0wtr.web.fc2.com/CookieClicker/")

        while True :
            try :
                # cookieボタン見つけてクリックさせる
                element = self.driver.find_element_by_id("bigCookie")
                element.click()

            except Exception as e :
                print(e)
