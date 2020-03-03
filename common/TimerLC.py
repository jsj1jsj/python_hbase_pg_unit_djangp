import threading
from bin import generatecase
from common import EmailSend
import time
import os
from common.PgSql import deleteOperate
from common.report_screenshot import reportscreenshot
import datetime
import shutil
from common.ReadAndWriteFiles import ReadAndWriteFiles
from common import globalB
from common.others import alter_text
from common.HbaseDeleData import deleteHbase
class TimerLM(object):
    @staticmethod
    def func():
        # 如果需要循环调用，就要添加以下方法
        delePG = deleteOperate()
        deleHb = deleteHbase()
        a1 = generatecase.Run()
        time.sleep(5)

        # 替换服务器html,json
        a = ReadAndWriteFiles()
        shutil.copy(os.path.join(a.path_testreport(), "result" + ".json"),
                     os.path.join(globalB.Gdjango_static_path, "report" + ".json"))
        path = shutil.copy(os.path.join(a.path_testreport(), "result" + ".html"),
                            os.path.join(globalB.Gdjango_templates_path, "report" + ".html"))
        # 替换服务器脚本
        new_str = '{% load static %}<script type="text/javascript" src="{% static "report.json" %}" charset="gbk"></script>'
        old_str = '<script type="text/javascript" src="result.json" charset="gbk"></script>'
        alter_text(path, old_str, new_str)

        # 截图
        b = reportscreenshot()
        # 发邮件
        EmailSend.sendmail(globalB.Gpng)
        # 获取现在时间
        now_time = datetime.datetime.now()
        # 获取明天时间
        next_time = now_time + datetime.timedelta(days=+1)
        next_year = next_time.date().year
        next_month = next_time.date().month
        next_day = next_time.date().day
        # 获取明天3点时间
        next_time = datetime.datetime.strptime(
            str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 08:00:00", "%Y-%m-%d %H:%M:%S")

        # 获取距离明天3点时间，单位为秒
        timer_start_time = (next_time - now_time).total_seconds()
        print(timer_start_time)
        timer = threading.Timer(timer_start_time, TimerLM.func)
        timer.start()

if __name__ == "__main__":
    b = TimerLM.func()



