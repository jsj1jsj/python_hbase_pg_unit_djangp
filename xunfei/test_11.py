# from common import globalB
from selenium import webdriver
import unittest
# from HTMLTestRunner import HTMLTestRunner
import time
from common import globalB
from common import ReadAndWriteFiles
from common import test_case_time_manager as TIME_MANAGER


class IndexSet():
    aIndex = 0

    @staticmethod
    def add():
        IndexSet.aIndex = IndexSet.aIndex + 1


class Request1( unittest.TestCase ):
    # '''三方支付-协议支付请求'''
    @classmethod
    def setUpClass(self):
        # 点击登录

        self.driver = webdriver.Chrome()  # 打开谷歌浏览器
        self.driver.implicitly_wait( TIME_MANAGER.TIME_OPEN_BROWSER_SEC )
        self.driver.maximize_window()
        self.driver.get( globalB.url_login )  # 访问路径
        self.driver.find_element_by_id( "username" ).send_keys( globalB.username )  # 输入登录用户名
        # 输入密码
        self.driver.find_element_by_id( "password" ).send_keys( globalB.password )  # 输入登录密码
        self.driver.find_element_by_xpath( '//*[@id="sublimtButton"]' ).click()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )

    def isElementExist(self, element):
        flag = True
        browser = self.driver
        try:
            browser.find_element_by_css_selector( element )
            return flag

        except:
            flag = False
            return flag

    def test_001(self):
        '''发送报文'''
        temp = ReadAndWriteFiles.ReadAndWriteFiles.read_case( "0" )
        self.driver.find_element_by_xpath( '//*[@id="nav"]/li[2]/a/cite' ).click()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        self.driver.find_element_by_xpath( '//*[@id="nav"]/li[2]/ul[1]/li/a/cite' ).click()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        frame1 = self.driver.find_element_by_xpath( '/html/body/div[3]/div/div[2]/div[2]/iframe' )
        self.driver.switch_to.frame( frame1 )
        self.driver.find_element_by_id( "hostport" ).send_keys( temp[IndexSet.aIndex]['端口'] )
        # 报文发送
        self.driver.find_element_by_id( "message" ).clear()
        self.driver.find_element_by_id( "message" ).send_keys( temp[IndexSet.aIndex]['请求报文1'] )  ##
        self.driver.find_element_by_xpath( '//*[@id="submit"]/i' ).click()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        if self.driver.find_element_by_xpath( '//*[@id="receive"]' ).get_attribute( "value" ) == "发送中。。。。":
            time.sleep( TIME_MANAGER.TIME_SEND_REPORT_DELAY_SEC )
            temp[IndexSet.aIndex]['实际结果1'] = self.driver.find_element_by_xpath( '//*[@id="receive"]' ).get_attribute(
                "value" )  # //
        else:
            temp[IndexSet.aIndex]['实际结果1'] = self.driver.find_element_by_xpath( '//*[@id="receive"]' ).get_attribute(
                "value" )  # //
        print( "期望结果1: " + temp[IndexSet.aIndex]['期望结果1'] )
        print( "实际结果1: " + temp[IndexSet.aIndex]['实际结果1'] )
        assert (temp[IndexSet.aIndex]['期望结果1'] in temp[IndexSet.aIndex]['实际结果1'])  # //
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )

    def test_002(self):  # 查询结果
        '''查询账号'''
        temp = ReadAndWriteFiles.ReadAndWriteFiles.read_case( "0" )
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath( '//*[@id="nav"]/li[1]/a' ).click()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        self.driver.find_element_by_xpath( '//*[@id="nav"]/li[1]/ul/li[1]/a/cite' ).click()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        self.driver.find_element_by_xpath( '//*[@id="nav"]/li[1]/ul/li[1]/ul/li[1]/a/cite' ).click()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        frame1 = self.driver.find_element_by_xpath( '/html/body/div[3]/div/div[2]/div[3]/iframe' )
        self.driver.switch_to.frame( frame1 )
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        self.driver.find_element_by_xpath( '//*[@id="account"]' ).send_keys(
            temp[IndexSet.aIndex]['查询账号2'].split( '/', 4 )[0] )  # /
        self.driver.find_element_by_xpath( '/html/body/div[2]/div/div/div/div[1]/form/div[2]/div' ).click()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        if temp[IndexSet.aIndex]['查询账号2'].split( '/', 4 )[1] == '三方支付':
            self.driver.find_element_by_xpath( '/html/body/div[2]/div/div/div/div[1]/form/div[2]/div/dl/dd[1]' ).click()
        elif temp[IndexSet.aIndex]['查询账号2'].split( '/', 4 )[1] == '手机银行':
            self.driver.find_element_by_xpath( '/html/body/div[2]/div/div/div/div[1]/form/div[2]/div/dl/dd[2]' ).click()
        elif temp[IndexSet.aIndex]['查询账号2'].split( '/', 4 )[1] == '个人网银':
            self.driver.find_element_by_xpath( '/html/body/div[2]/div/div/div/div[1]/form/div[2]/div/dl/dd[3]' ).click()
        elif temp[IndexSet.aIndex]['查询账号2'].split( '/', 4 )[1] == '自助银行':
            self.driver.find_element_by_xpath( '/html/body/div[2]/div/div/div/div[1]/form/div[2]/div/dl/dd[4]' ).click()
        elif temp[IndexSet.aIndex]['查询账号2'].split( '/', 4 )[1] == '电话银行':
            self.driver.find_element_by_xpath( '/html/body/div[2]/div/div/div/div[1]/form/div[2]/div/dl/dd[5]' ).click()
        elif temp[IndexSet.aIndex]['查询账号2'].split( '/', 4 )[1] == '信用卡APP':
            self.driver.find_element_by_xpath( '/html/body/div[2]/div/div/div/div[1]/form/div[2]/div/dl/dd[6]' ).click()
        elif temp[IndexSet.aIndex]['查询账号2'].split( '/', 4 )[1] == '逻辑柜面':
            self.driver.find_element_by_xpath( '/html/body/div[2]/div/div/div/div[1]/form/div[2]/div/dl/dd[7]' ).click()
        elif temp[IndexSet.aIndex]['查询账号2'].split( '/', 4 )[1] == '统一柜面':
            self.driver.find_element_by_xpath( '/html/body/div[2]/div/div/div/div[1]/form/div[2]/div/dl/dd[8]' ).click()
        elif temp[IndexSet.aIndex]['查询账号2'].split( '/', 4 )[1] == 'POS':
            self.driver.find_element_by_xpath( '/html/body/div[2]/div/div/div/div[1]/form/div[2]/div/dl/dd[9]' ).click()
        elif temp[IndexSet.aIndex]['查询账号2'].split( '/', 4 )[1] == '银联前置':
            self.driver.find_element_by_xpath(
                '/html/body/div[2]/div/div/div/div[1]/form/div[2]/div/dl/dd[10]' ).click()
        self.driver.find_element_by_xpath( '//*[@id="startTime"]' ).send_keys(
            temp[IndexSet.aIndex]['查询账号2'].split( '/', 4 )[2] )  # //
        self.driver.find_element_by_xpath( '//*[@id="endTime"]' ).send_keys(
            temp[IndexSet.aIndex]['查询账号2'].split( '/', 4 )[3] )  # //
        self.driver.find_element_by_xpath( '//*[@id="submit"]/i' ).click()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        temp[IndexSet.aIndex]['实际结果2'] = self.driver.find_element_by_xpath( '//*[@id="dataResult"]' ).get_attribute(
            'value' )
        print( "期望结果2: " + temp[IndexSet.aIndex]['期望结果2'] )
        print( "实际结果2: " + temp[IndexSet.aIndex]['实际结果2'] )
        assert (temp[IndexSet.aIndex]['期望结果2'] in temp[IndexSet.aIndex]['实际结果2'])  # //

    def test_003(self):
        '''查询短信'''
        temp = ReadAndWriteFiles.ReadAndWriteFiles.read_case( "0" )
        self.driver.switch_to.default_content()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        self.driver.find_element_by_xpath( '//*[@id="nav"]/li[1]/ul/li[1]/ul/li[4]/a/cite' ).click()
        self.driver.implicitly_wait( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        frame1 = self.driver.find_element_by_xpath( '/html/body/div[3]/div/div[2]/div[4]/iframe' )
        self.driver.switch_to.frame( frame1 )
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        self.driver.find_element_by_xpath( '//*[@id="account"]' ).send_keys(
            temp[IndexSet.aIndex]['查询短信3'].split( '/', 2 )[0] )  # /
        self.driver.find_element_by_xpath( '//*[@id="certificate"]' ).send_keys(
            temp[IndexSet.aIndex]['查询短信3'].split( '/', 2 )[1] )  # //
        self.driver.find_element_by_xpath( '//*[@id="submit"]/i' ).click()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        flag = Request1.isElementExist( self, '#msgResult > tr > th' )
        if flag:
            temp[IndexSet.aIndex]['实际结果3'] = self.driver.find_element_by_xpath( '//*[@id="msgResult"]/tr/th' ).text
        else:
            temp[IndexSet.aIndex]['实际结果3'] = self.driver.find_element_by_xpath(
                '//*[@id="msgResult"]/tbody[1]/tr/td[2]' ).text

        print( "期望结果3: " + temp[IndexSet.aIndex]['期望结果3'] )
        print( "实际结果3: " + temp[IndexSet.aIndex]['实际结果3'] )
        assert (temp[IndexSet.aIndex]['期望结果3'] in temp[IndexSet.aIndex]['实际结果3'])  # //

    def test_004(self):
        '''查询外呼'''
        # index = IndexSet.aInd
        temp = ReadAndWriteFiles.ReadAndWriteFiles.read_case( "0" )
        self.driver.switch_to.default_content()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        self.driver.find_element_by_xpath( '//*[@id="nav"]/li[1]/ul/li[1]/ul/li[5]/a/cite' ).click()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        frame1 = self.driver.find_element_by_xpath( '/html/body/div[3]/div/div[2]/div[5]/iframe' )
        self.driver.switch_to.frame( frame1 )
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        self.driver.find_element_by_xpath( '//*[@id="account"]' ).send_keys(
            temp[IndexSet.aIndex]['查询外呼4'].split( '/', 2 )[0] )  # //
        self.driver.find_element_by_xpath( '//*[@id="certificate"]' ).send_keys(
            temp[IndexSet.aIndex]['查询外呼4'].split( '/', 2 )[1] )  # //
        self.driver.find_element_by_xpath( '//*[@id="submit"]/i' ).click()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        flag = Request1.isElementExist( self, '#msgResult > tr > th' )
        if flag:
            temp[IndexSet.aIndex]['实际结果4'] = self.driver.find_element_by_xpath( '//*[@id="msgResult"]/tr/th' ).text
        else:
            temp[IndexSet.aIndex]['实际结果4'] = self.driver.find_element_by_xpath(
                '//*[@id="msgResult"]/tbody[1]/tr/td[2]' ).text
        print( "期望结果4: " + temp[IndexSet.aIndex]['期望结果4'] )
        print( "实际结果4: " + temp[IndexSet.aIndex]['实际结果4'] )
        assert (temp[IndexSet.aIndex]['期望结果4'] in temp[IndexSet.aIndex]['实际结果4'])  # //

    def test_005(self):
        '''查询疑似风险交易'''
        temp = ReadAndWriteFiles.ReadAndWriteFiles.read_case( "0" )
        self.driver.switch_to.default_content()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        self.driver.find_element_by_xpath( '//*[@id="nav"]/li[1]/ul/li[1]/ul/li[6]/a/cite' ).click()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        frame1 = self.driver.find_element_by_xpath( '/html/body/div[3]/div/div[2]/div[6]/iframe' )
        self.driver.switch_to.frame( frame1 )
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        self.driver.find_element_by_xpath( '//*[@id="account"]' ).send_keys(
            temp[IndexSet.aIndex]['查询疑似风险交易5'].split( '/', 2 )[0] )  # //
        self.driver.find_element_by_xpath( '//*[@id="certificate"]' ).send_keys(
            temp[IndexSet.aIndex]['查询疑似风险交易5'].split( '/', 2 )[1] )  # //
        self.driver.find_element_by_xpath( '//*[@id="submit"]/i' ).click()
        time.sleep( TIME_MANAGER.TIME_INQUIRE_REPORT_DELAY_SEC )
        flag = Request1.isElementExist( self, '#msgResult > tr > th' )
        if flag:
            temp[IndexSet.aIndex]['实际结果5'] = self.driver.find_element_by_xpath( '//*[@id="msgResult"]/tr/th' ).text
        else:
            temp[IndexSet.aIndex]['实际结果5'] = self.driver.find_element_by_xpath(
                '//*[@id="msgResult"]/tbody[1]/tr/td[7]' ).text
        print( "期望结果5: " + temp[IndexSet.aIndex]['期望结果5'] )
        print( "实际结果5: " + temp[IndexSet.aIndex]['实际结果5'] )
        # assert (temp[IndexSet.aIndex]['期望结果5'] in temp[IndexSet.aIndex]['实际结果5'])  # //
        # IndexSet.add()
        try:
            assert (temp[IndexSet.aIndex]['期望结果5'] in temp[IndexSet.aIndex]['实际结果5'])  # //
            IndexSet.add()
        except AssertionError as e:
            IndexSet.add()
            raise

    @classmethod
    def tearDownClass(self):
        self.driver.close()


# if __name__ == "__main__":
#     unittest.main()
if __name__ == "__main__":
    globalB.testunit.addTest( Request1( "test_case1" ) )
