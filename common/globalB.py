
import threading
# class Singleton(object):
#     _instance_lock = threading.Lock()
#     list map
#     def __init__(self):
#         pass
#
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"):
#             with Singleton._instance_lock:
#                 if not hasattr(Singleton, "_instance"):
#                     Singleton._instance = object.__new__(cls)
#         return Singleton._instance

# 登录相关
import unittest
global Gdriver
Gdriver = ''
global url_login
url_login='http://10.136.1.77:8090/dataquery/home/main'
global username
username='admin1'
global password
password='111111'
global duankouShu
duankouShu='10.136.1.96:11111'
global duankouJs
duankouJs='10.136.1.96:22222'

# 控制用例相关
global Cnum
Cnum=''
global CcsvName
CcsvName=''
global CbookName
CcaseName=''
global CstartRow
CstartRow=''
global CendRow
CendRow=''
global Cpass
Cpass=''
global Cfail
Cfail=''
global CpassSum
CpassSum=''
global CfailSum
CfailSum=''
global CsheetNames
CsheetNames=''
global CsheetName
CsheetName=''
global CsheetNum
CsheetNum=''
global CsheetObject
CsheetObject=''
global CsheetIndex
CsheetIndex=''
global CsheetRows
CsheetRows=''
global CsheetCols
CsheetCols=''

#规则相关
global Rnum
Rnum=''
global RcaseDes
RcaseDes=''
global Rmethod
Rmethod=''
global Rrequest1
Rrequest1=''
global RexpectedResult1
RexpectedResult1=''
global Rsearch2
Rsearch2=''
global RexpectedResult2
RexpectedResult2=''
global Rsearch3
Rsearch3=''
global RexpectedResult3
RexpectedResult3=''
global Rsearch4
Rsearch4=''
global RexpectedResult4
RexpectedResult4=''

global RrealResult1
RrealResult1=''
global RrealResult2
RrealResult2=''
global RrealResult3
RrealResult3=''
global RrealResult4
RrealResult4=''
global RtestResult1  #pass/fail
RtestResult1='1'
global RtestResult2  #pass/fail
RtestResult2=''
global RtestResult3  #pass/fail
RtestResult3=''
global RtestResult4  #pass/fail
RtestResult4=''
global RpassResult
RpassResult=''
global RfailResult
RfailResult=''
global RpassAllResult
RpassAllResult=''
global RfailAllResult
RfailAllResult=''


#生成报告
global testunit
testunit=unittest.TestSuite()



#索引
global index
index=6

#django服务器地址
global Gdango_static_path
Gdjango_static_path = r'D:\xunfei20200117bk\billy_home-Report_server-master\Report_server\static'

global Gdjango_templates_path
Gdjango_templates_path = r'D:\xunfei20200117bk\billy_home-Report_server-master\Report_server\templates'

global Gpng
Gpng = ''




