#coding=utf-8
import os
import configparser as cparser
import csv
import xlrd

class ReadAndWriteFiles(object):
    def __init__(self):
        self.path_data()
        self.path_casesource()
        self.path_report_xml()
        self.path_rob()
        self.path_report_email()

    def path_data(self):
        '''
        :return: 返回Data.csv的绝对路径
        '''
        current_path = os.path.abspath(__file__)
        config_file_path = os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."),'config_file/Data.csv')
        pathdata1 = config_file_path.replace("\\", "/")
        pathdata2 = pathdata1.replace("/", "\\")
        self.pathdata = pathdata2
    def path_casesource(self):
        '''
        :return: 返回casesource的绝对路径
        '''
        current_path = os.path.abspath(__file__)
        pathcasesource = os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."),'testcase/control.xlsx')
        pathcasesource1 = pathcasesource.replace("\\", "/")
        pathcasesource2 = pathcasesource1.replace("/", "\\")
        self.pathcasesource = pathcasesource2

    def path_casedir(self):
        '''
        :return: 返回casesource的绝对路径
        '''
        current_path = os.path.abspath(__file__)
        pathcasedir = os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."),'testcase')
        pathcasedir1 = pathcasedir.replace("\\", "/")
        pathcasedir2 = pathcasedir1.replace("/", "\\")
        return pathcasedir2
        # self.pathcasedir = pathcasedir2

    def path_testreport(self):
        '''
        :return: 返回casesource的绝对路径
        '''
        current_path = os.path.abspath(__file__)
        pathreport = os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."), 'report')
        pathreport1 = pathreport.replace("\\", "/")
        pathreport2 = pathreport1.replace("/", "\\")
        return pathreport2

    def path_screenshotreport(self):
        '''
        :return: 返回casesource的绝对路径
        '''
        current_path = os.path.abspath( __file__ )
        screenshotreport = os.path.join( os.path.abspath( os.path.dirname(current_path) + os.path.sep + ".." ), 'report_png' )
        screenshotreport1 = screenshotreport.replace( "\\", "/" )
        screenshotreport2 = screenshotreport1.replace( "/", "\\" )
        return screenshotreport2
    def path_caseRun(self,name):
        '''
        :return: 返回casesource的绝对路径
        '''
        current_path = os.path.abspath(__file__)
        temp="testcase/"+ name +".xlsx"
        print(temp)
        pathresourse = os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."),temp)
        pathdata1 = pathresourse.replace("\\", "/")
        # print('pathdata1:' + pathdata1)
        pathdata2 = pathdata1.replace("/", "\\")
        # print('pathdata2:' + pathdata2)
        return pathdata2

    def path_report_xml(self):
        '''
        :return: 返回HostUrl.ini的绝对路径
        '''
        current_path = os.path.abspath(__file__)
        pathreportxml = os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."),'report/output.xml')
        # pathreportxml = pathreportxml.replace("\\", "/")
        self.pathreportxml = pathreportxml
    def path_report_email(self):
        '''
        :return: 返回email.ini绝对路径
        '''
        current_path = os.path.abspath(__file__)
        pathemailini = os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."),'config_file\Email.ini')
        self.pathemailini = pathemailini

    def path_rob(self):
        '''
        :return: 返回HostUrl.ini的绝对路径
        '''
        current_path = os.path.abspath(__file__)
        pathrob = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "..")
        # pathrob = pathrob.replace("\\", "/")
        self.pathrob = pathrob

    def ini_read1(self,filepath):
        date = csv.reader(open(filepath,'r'))
        for line in date:
            url = line[0]
            username = line[1]
            password = line[2]
            # print(line)
            return line
            # print("url:" + url)
            # print("username:" + username)
            # print("password:" + password)
            #
            # return url,username,password
    def ini_read(self,filepath,value):
        '''
        :param filepath: 加载文件地址
        :param value: 读取的键
        :return: 对应键的值
        '''
        cfb = cparser.ConfigParser()
        cfb.read(filepath, encoding="utf-8-sig")
        v = cfb.get("test", value)
        return v

    def read_case(self):
        a = ReadAndWriteFiles()
        path = a.pathcasesource
        work_book = xlrd.open_workbook(path)
        work_sheet = work_book.sheet_by_index( 0 )

        # 获取总行数
        total_rows = work_sheet.nrows

        # 定义一个列表，用于存放每一行的内容
        data_list = []
        key_list = None
        for i in range( total_rows ):
            # 获取每一行的内容
            row_data = work_sheet.row_values( i )
            if i == 0:
                # 将第一行的作为字典的key
                key_list = row_data
            else:

                data_dict = dict()
                for index, cel_data in enumerate( row_data ):
                    # 获取字典的key
                    key = key_list[index]

                    # 注意点01 : 如果该单元格存放的是日期类型，读入的时候，需要借助 xldate_as_datetime 模块
                    # 具体的用法请自行百度
                    if index == 28:
                        if cel_data:
                            cel_data = xldate_as_datetime(cel_data, 0)
                    else:
                        # 注意点02: 单元格是数字的，读取时会识别为浮点数，特此处理一下
                        if isinstance( cel_data, float ):
                            cel_data = int( cel_data )

                    # 字典赋值
                    data_dict[key] = cel_data
                # 将字典加入需要返回的列表中
                data_list.append(data_dict)
        # self.read_case()=data_list
        return data_list

    def ini_write(self,filepath,section,key,value):
        '''
        :param filepath: 加载文件地址
        :param value: 读取的键
        :return: 对应键的值
        '''
        cfb = cparser.ConfigParser()
        cfb.read(filepath, encoding="utf-8-sig")
        cfb.set(section,key,value)
        cfb.write(open(filepath, "r+"))

if __name__=="__main__":
    a = ReadAndWriteFiles()
    q=a.read_case()
    # for i in q:
    #     print(q)
    print(q[0]['编号'])
    # # date=csv.reader(open(a.pathcasesource,'r')) D:/XunFei/config_file/Email.ini
    # # for d in date:
    # #     print(d)
    # # a=ReadAndWriteFiles()
    # path=a.pathcasesource
    # # x1 = xlrd.open_workbook(path)
    # test_dir = a.path_casedir()
    # print(test_dir)



