# from common import globalB
from selenium import webdriver
import unittest
# from HTMLTestRunner import HTMLTestRunner
import time
from common import globalB
from common import ReadAndWriteFilesbk





driver = webdriver.Chrome()  # 打开谷歌浏览器
driver.implicitly_wait(1)
driver.maximize_window()
driver.get(globalB.url_login)  # 访问路径
'''发送报文'''
# index = IndexSet.aIndex
print(IndexSet.aIndex)
temp = ReadAndWriteFilesbk.ReadAndWriteFiles.read_case( "0" )
# # 输入用户名
driver.find_element_by_id("username").send_keys(globalB.username)  # 输入登录用户名
# 输入密码
driver.find_element_by_id("password").send_keys(globalB.password)  # 输入登录密码
driver.find_element_by_xpath('//*[@id="sublimtButton"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="nav"]/li[2]/a/cite').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="nav"]/li[2]/ul[1]/li/a/cite').click()
time.sleep(1)
frame1 = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/iframe')
driver.switch_to.frame(frame1)
driver.find_element_by_id("hostport").send_keys(temp[IndexSet.aIndex]['端口'])
# 报文发送
driver.find_element_by_id("message").clear()
driver.find_element_by_id("message").send_keys(temp[IndexSet.aIndex]['请求报文1'])##
driver.find_element_by_xpath('//*[@id="submit"]/i').click()
time.sleep(1)
temp[IndexSet.aIndex]['实际结果1'] = driver.find_element_by_xpath('//*[@id="receive"]').get_attribute("value")#//
print("期望结果1: "+temp[IndexSet.aIndex]['期望结果1'])
print("实际结果1:"+temp[IndexSet.aIndex]['实际结果1'])
assert (temp[IndexSet.aIndex]['期望结果1'] in temp[IndexSet.aIndex]['实际结果1'])#//
time.sleep(1)


