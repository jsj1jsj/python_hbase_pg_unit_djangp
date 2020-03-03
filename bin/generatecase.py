# coding=utf-8
import sys
import types
from common.ReadAndWriteFiles import ReadAndWriteFiles
from common import globalB
from bin.init import *
from HTMLTestRunner import HTMLTestRunner
import os
import unittest
from xunfei import test_11
from common import TimerLC
import datetime

def RunJson(self,request1,request2,request3,reqest4):
    current_path = os.path.abspath(__file__)
    config_file_path = os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."),'config_file/Data.csv')
    pathdata1 = config_file_path.replace("\\", "/")
    pathdata2 = pathdata1.replace("/", "\\")
    self.pathdata = pathdata2

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getatime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new
    pass


def Run():
    a=ReadAndWriteFiles()
    path=a.pathcasesource
    # x1 = xlrd.open_workbook(path)
    # test_dir = a.path_casedir()
    test_report=a.path_testreport()
    # globalB.CsheetRows = x1.sheet_by_name("control").nrows
    datalist = a.read_case()
    globalB.CsheetRows = len(datalist)
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = test_report + '\\' + 'result.html'
    # filename = test_report + '\\' + now + 'result.html'
    globalB.Gdriver=filename
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    testunit = unittest.TestSuite()
    loader = unittest.defaultTestLoader
    # for i in range(test_11.IndexSet.aIndex, globalB.CsheetRows):
    for i in range(test_11.IndexSet.aIndex,1):
        new_cls = type("用例" + str(i+1), (test_11.Request1,), {})
        new_cls.__doc__ = datalist[i]['用例描述']
        test_cases = loader.loadTestsFromTestCase(new_cls)
        if(test_cases != None):
            testunit.addTests(test_cases)
    runner.run(testunit)
    fp.close()

if __name__ == "__main__":
    now_time = datetime.datetime.now()
    print("现在时间" + str(now_time))
    next_year = now_time.date().year
    print("今天年" + str(next_year))
    next_month = now_time.date().month
    print("今天月" + str(next_month))
    next_day = now_time.date().day
    print("今天日" + str(next_day))
    # # 获取明天时间
    # next_time = now_time + datetime.timedelta(days=+1)
    # print("明天时间" + str(next_time))
    # next_year = next_time.date().year
    # print("明天年" + str(next_year))
    # next_month = next_time.date().month
    # print("明天月" + str(next_month))
    # next_day = next_time.date().day
    # print("明天日" + str(next_day))
    # 获取明天跑脚本时间
    next_time = datetime.datetime.strptime(str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 00:15:00", "%Y-%m-%d %H:%M:%S")
    print("明天跑脚本时间" + str(next_time))

    # 获取距离明天8点时间，单位为秒
    timer_start_time = (next_time - now_time).total_seconds()
    print("距离明天跑脚本时间，单位为秒:" + str(timer_start_time))

    # 定时器,参数为(多少时间后执行，单位为秒，执行的方法)
    timer = threading.Timer(timer_start_time, TimerLC.TimerLM.func)
    print("定时时间" + str(timer))
    timer.start()
