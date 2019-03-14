from Sample import Sample
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re

class Sample2(Sample):   
    #お店をクリックする（100回以下は無視)
    def upgradsClick(self):
        if self.loopCount < 100:
            return
        try:
            #<div onclick="Game.UpgradesById[56].click(event);" 
            # Game.tooltip.wobble();}" id="upgrade1" style="background-position:-528px -144px;"></div>
            for var in range(0,1000):
                element = self.driver.find_element_by_id("upgrade" + str(var))
                element.click()              
        except Exception as e :
            print("productClick:"+ str(e))  
    
    #施設をクリックする（100回以下は無視)
    def productClick(self) :
        if self.loopCount < 100:
            return
        for var in reversed(range(0,20)):           
            try:
                #要素の検証したらIDがproduct+連番だった。
                #<div class="product unlocked enabled" onmouseout="Game.tooltip.shouldHide=1;
                # " id="product0"><div class="icon off" id="productIconOff0" style="background-position:
                #要素の数は適当
                    element = self.driver.find_element_by_id("product" + str(var))
                    element.click()
            except Exception as e :
                print(e)

    # ループのカウンタを定義して初期化
    def initLoopCount(self):
        self.loopCount = 0

    # ループカウンタを加算。100を超えてる場合は戻す
    def addLoopCount(self):
        if (self.loopCount < 100) :
            self.loopCount = self.loopCount + 1
        else:
            self.loopCount = 0
    #メソッドリストにぶち込む
    def getBeforeExecFunctions(self):
        super().getBeforeExecFunctions()
        self.beforeExecFunctions.append(self.initLoopCount)

    def getDoExecFunctions(self):
        super().getDoExecFunctions()
        self.doExecFunctions.append(self.upgradsClick) 
        self.doExecFunctions.append(self.productClick)

    def getAfterDoExecFunctions(self):
        super().getAfterDoExecFunctions()
        self.afterDoExecFunctions.append(self.addLoopCount)
