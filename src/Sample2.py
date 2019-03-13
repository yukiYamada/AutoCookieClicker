from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re

class Sample2:
    
    # driverpath=各種Webドライバーexeのフルパス
    def __init__(self, driverpath):
        # ドライバーパスを指定 
        self.driver = webdriver.Chrome(driverpath)

    #左側のでかいクッキー連打
    def bigCookieClick(self):
        try :
            # cookieボタン見つけてクリックさせる
            element = self.driver.find_element_by_id("bigCookie")
            element.click()
        except Exception as e :
            print(e)
    #お店をクリックする
    def upgradsClick(self):
        try:
            #<div onclick="Game.UpgradesById[56].click(event);" 
            # Game.tooltip.wobble();}" id="upgrade1" style="background-position:-528px -144px;"></div>
            for var in range(0,1000):
                element = self.driver.find_element_by_id("upgrade" + str(var))
                element.click()              
        except Exception as e :
            print("productClick:"+ str(e))  
    #施設をクリックする
    def productClick(self) :
        for var in reversed(range(0,20)):
            try:
                #要素の検証したらIDがproduct+連番だった。
                #<div class="product unlocked enabled" onmouseout="Game.tooltip.shouldHide=1;
                # " id="product0"><div class="icon off" id="productIconOff0" style="background-position:
                #要素の数は適当
                    element = self.driver.find_element_by_id("product" + str(var))
                    element.click()
            except Exception as e :
                print("productClick:"+ str(e))

    def exec(self):
        # URLに移動
        self.driver.get("http://natto0wtr.web.fc2.com/CookieClicker/")
        clickcount = 0
        while True :
            self.bigCookieClick()
            if clickcount > 100:
                #効率悪いから強化はとりあえず100回に1回
                clickcount = 0
                self.upgradsClick()
                self.productClick()
            clickcount = clickcount + 1
            
            

