from Sample2 import Sample2
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import datetime
from GetElepsed import GetElepsed
from operator import itemgetter

#コスト関連https://www55.atwiki.jp/cookieclickerjpn/pages/7.html
class Sample3(Sample2):
    def setCheckTime(self):
        self.checkTime =  datetime.datetime.now()
    # 初期処理（コンストラクタめんどくせ）
    def sample3init(self):
        self.totalProducts = 0
        self.million = 1000000
        self.billion = 100000000
        self.trillion = 10000000000
        self.quadrillion = 10000000000000
        # 10秒ごとに施設購入を検討する
        self.waitTimeMax = 10
        self.setCheckTime()
        self.failCount = 0
    #施設CPS
    def puroductCPS(self, productNo):
        cps = 0
        if(productNo == 0):
            cps = 0.1
        elif(productNo == 1):
            cps = 1
        elif(productNo == 2):
            cps = 8
        elif(productNo == 3):
            cps = 47
        elif(productNo == 4):
            cps = 260
        elif(productNo == 5):
            cps = 1400
        elif(productNo == 6):
            cps = 7800
        elif(productNo == 7):
            cps = 44000
        elif(productNo == 8):
            cps = 260000
        elif(productNo == 9):
            cps = 1.6 * self.million
        elif(productNo == 10):
            cps = 10 * self.million
        elif(productNo == 11):
            cps = 65 * self.million
        elif(productNo == 12):
            cps = 430 * self.million
        elif(productNo == 13):
            cps = 2.9 * self.billion
        elif(productNo == 14):
            cps = 21 * self.billion
        elif(productNo == 15):
            cps = 150 * self.billion

        return cps

    #施設の単価
    def productsCost(self, productNo):
        cost = 0
        if(productNo == 0):
            cost = 15
        elif(productNo == 1):
            cost = 100
        elif(productNo == 2):
            cost = 1100
        elif(productNo == 3):
            cost = 12000
        elif(productNo == 4):
            cost = 130000
        elif(productNo == 5):
            cost = 1.4 * self.million
        elif(productNo == 6):
            cost = 20 * self.million
        elif(productNo == 7):
            cost = 330 * self.million
        elif(productNo == 8):
            cost = 5.1 * self.billion
        elif(productNo == 9):
            cost = 75 * self.billion
        elif(productNo == 10):
            cost = 1 * self.trillion
        elif(productNo == 11):
            cost = 14 * self.trillion
        elif(productNo == 12):
            cost = 170 * self.trillion
        elif(productNo == 13):
            cost = 2.1 * self.quadrillion
        elif(productNo == 14):
            cost = 26 * self.quadrillion
        elif(productNo == 15):
            cost = 310 * self.quadrillion            

        # 最初以外は総施設数の1.15倍
        multiple = self.productsOwned(productNo) * 1.15 if self.productsOwned(productNo) != 0 else 1
        return cost * multiple
    
    # 所持数
    def productsOwned(self, productNo):
        try:
            element = self.driver.find_element_by_id("productOwned" + str(productNo))
            text = element.text
            if not text:
                text = "0"
            
            return int(text) 
        except Exception as e:
            print(e)

    #　費用対効果
    def cpsPerPrice(self, productNo):
        cost = self.productsCost(productNo)
        cps = self.puroductCPS(productNo)

        return cps / cost
    
    # 最も費用対効果順にならびかえ
    def mostCpsProduct(self):
        try:
            ret = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0]]
            for var in (range(0,15)):
                ret[var] = [var,self.cpsPerPrice(var)]
            return sorted(ret, key = itemgetter(1), reverse = True)
        except Exception as e:
            print(e)
    def buy(self,productNo):
        # 買えるだけ買う
        while(True):
            # 万とかなんとか桁の漢字を使ってくるので、Cookiesを取得するのが面倒だから、
            # ownedの増加で買えたかどうか。を判定する
            preClickOwned = self.productsOwned(productNo)              
            try:
                element = self.driver.find_element_by_id("product" + str(productNo))
                element.click()
            except Exception:
                # オブジェクトがない。とかは無視（購入できなかった
                break
            clickedOwned = self.productsOwned(productNo)
            if(preClickOwned != clickedOwned):
                self.totalProducts = self.totalProducts + 1
                return True
                break
            else:
                # Cookiesが足りない。購入できなかった。
                break
        return False

    def productClick(self) :
        elepsed = GetElepsed.getElepsedNow(self.checkTime)
        if(elepsed < self.waitTimeMax):
            return
        self.setCheckTime()

        # 厳密には再計算がいるけど、誤差だろう
        productNos = self.mostCpsProduct()
        # 高効率Topを購入できるだけ買う
        success =  self.buy(productNos[0][0])
        if success :
            return
 
        self.failCount = self.failCount + 1
        if self.failCount < 3:
            return

        #3回(30秒)も失敗するなら適当に買ったほうが早い 
        self.failCount = 0
        for var in productNos:
            # 買えるだけ買う
            self.buy(var[0])

    def init(self):
        super().init()

    #メソッドリストにぶち込む
    def getBeforeExecFunctions(self):
        super().getBeforeExecFunctions()
        self.beforeExecFunctions.append(self.sample3init)


