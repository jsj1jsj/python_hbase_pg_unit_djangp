from common.globalB import *
from bin.init import *
import time
from selenium import webdriver

def RunShuxian(request1, request2, request3, reqest4):
    #  打开浏览器，并定义打开实例为driver
    driver = webdriver.Chrome()
    # 隐性时间等待20s
    driver.implicitly_wait(5)

    # # 打开登录页面*************************************1112*******************************************************
    driver.get(url_login)
    # # 输入用户名
    driver.find_element_by_id("username").send_keys(username)  # 输入登录用户名
    # 输入密码
    driver.find_element_by_id("password").send_keys(password)  # 输入登录密码
    # 点击登录
    driver.find_element_by_xpath('//*[@id="sublimtButton"]').click()
    driver.maximize_window()
    # 报文发送
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="nav"]/li[2]/a/cite').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="nav"]/li[2]/ul[1]/li/a/cite').click()

    # 规则11第三方协议支付
    time.sleep(5)
    frame1 = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/iframe')
    driver.switch_to_frame(frame1)
    driver.find_element_by_id("hostport").send_keys(duankouShu)
    driver.find_element_by_id("message").send_keys(request1)
    driver.find_element_by_xpath('//*[@id="submit"]/i').click()
    time.sleep(5)

    RrealResult1 = driver.find_element_by_xpath('//*[@id="receive"]').get_attribute("value")
    time.sleep(15)
    time.sleep(15)

    if RexpectedResult1 in RrealResult1:
        RtestResult1 = "pass"
    else:
        RtestResult1 =  "fail"
    driver.switch_to.default_content()
    driver.find_element_by_xpath('//*[@id="nav"]/li[1]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="nav"]/li[1]/ul/li[1]/a/cite').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="nav"]/li[1]/ul/li[1]/ul/li[1]/a/cite').click()
    time.sleep(5)
    frame1 = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/iframe')
    driver.switch_to_frame(frame1)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="account"]').send_keys(request2.split('/',4)[0])
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/form/div[2]/div/div/input').send_keys(request2.split('/',4)[1])
    driver.find_element_by_xpath('//*[@id="startTime"]').send_keys(request2.split('/',4)[2])
    driver.find_element_by_xpath('//*[@id="endTime"]').send_keys(request2.split('/',4)[3])
    driver.find_element_by_xpath('//*[@id="submit"]/i').click()
    time.sleep(1)

    RrealResult2 = driver.find_element_by_xpath('//*[@id="dataResult"]').get_attribute('value')
    time.sleep(15)

    if RexpectedResult2 in RrealResult2:
        RtestResult2 = "pass"
    else:
        RtestResult2 =  "fail"
    driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a').click()
    driver.close()
    return RrealResult1,RrealResult2,RrealResult3,RrealResult4,RtestResult1,RtestResult2,RtestResult3,RtestResult4
if __name__=="__main__":
    request1='|11|100001|1149521315172200063|1149521315172200063|0681912131517220168|0004|6210986905210020582|1|1|20191010101010|10.00|2|01|||||||20191009101010|||1|110100199401027789||||||0|||||'
    request2='6210986905210020511/三方支付/2019-12-27 10:00:00/2019-12-27 11:00:00'
    l=request2.split('/',4)[3]
    request3='1'
    request4='2'
    RunShuxian(request1, request2, request3, request4)


