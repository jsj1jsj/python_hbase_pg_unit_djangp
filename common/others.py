# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 16:01
# @Author  : billy
# @File    : others.py

import os
import re
import inspect
import time
import subprocess
import datetime

project_path = os.path.dirname(os.path.dirname(__file__))


def run_command(cmd_line):

    a = subprocess.getoutput(cmd_line)
    print(a)

# cmd_line = 'python e:\\111.py'


def get_caseno(self):
    """获取当前运行的类名、方法名"""
    # class_name = self.__class__.__name__

    context=inspect.stack()[2]   #获取堆内存，不一定是第二条，需要具体分析
    func_name= re.search("function='test_(.+?)'",str(context)).group(1)

    sheet_name = func_name.split("_")[0]
    row_no = func_name.split("_")[1]
    return [sheet_name,row_no]

def get_current_function_name():
    return inspect.stack()[1][3]

#替换文件中的字符串
def alter_text(file, old_str, new_str):
    """
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)

def get_now():
    a=time.time()
    a=int(a*1000)
    return a


#测试结果比较
def compare_data(type, expect_data, actual_data):
    """
    :param type: 0-完全匹配，1-局部匹配
    :param expect_data: 预期结果
    :param actual_data: 实际结果
    """
    if type == 0:
        if isinstance(expect_data, dict):     # 判断expect_data格式为字典
            for key in actual_data:           # 遍历actual_data的key，判断是否都在expect_data中存在
                assert(key in expect_data.keys()), "实际返回结果中的key值%s 不在预期结果中" % key

            for key in expect_data:           # 遍历expect_data的key，判断是否都在actual_data中存在，如果存在继续递归
                if key in actual_data:
                    compare_data(0, expect_data[key], actual_data[key])
                else:
                    assert(key in actual_data.keys()), "预期结果中的key值%s 不在实际返回结果中" % key

        elif isinstance(expect_data, list):    # 判断expect_data格式为列表
            assert(len(expect_data) == len(actual_data))    # 比较列表的个数
            for index,value in enumerate(expect_data):      # 遍历预期列表数据并获取角标
                if isinstance(value, dict):
                    assert isinstance(actual_data[index],dict)
                    compare_data(0,value,actual_data[index])

                if isinstance(value, list):
                    for src_list, dst_list in zip(sorted(expect_data), sorted(actual_data)):
                        compare_data(0, src_list, dst_list)
        else:
            assert(str(expect_data)==str(actual_data)), expect_data + "!=" + actual_data

    if type == 1:
        if isinstance(expect_data, dict):  # 判断src格式为字典
            for key in expect_data:
                if key in str(actual_data):
                    assert(str(expect_data[key]) in str(actual_data)),"预期结果%s不在返回集中"%str(expect_data[key])
                else:
                    assert(key in str(actual_data))

        elif isinstance(expect_data, list):  # 判断src格式为字典
            assert(str(expect_data) in str(actual_data))

        else:
            assert (str(expect_data) == str(actual_data)), "预期结果->%s 不等于实际结果%s"(str(expect_data), str(actual_data))


def opera_datatime(days):
    """加减当前日期的算法"""
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=days)
    n_days = now + delta
    return n_days



if __name__=="__main__":
    print(project_path)