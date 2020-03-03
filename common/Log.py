import os
class MyLog(object):
    # def __init__(self):
    #     self.path_pie()

    def get_log(self):
        '''
        :return: pie的绝对路径
        '''
        current_path = os.path.abspath(__file__)
        config_file_path = os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."),'report_png')
        pathdata1 = config_file_path.replace("\\", "/")
        pathdata2 = pathdata1.replace("/", "\\")
        return pathdata2