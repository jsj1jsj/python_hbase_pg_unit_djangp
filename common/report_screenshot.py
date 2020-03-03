from selenium import webdriver
import time,datetime
from common import globalB
from common.ReadAndWriteFiles import ReadAndWriteFiles
from common import test_case_time_manager

def reportscreenshot():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)  # 打开谷歌浏览器
    driver.maximize_window()
    js_height = "return document.body.clientHeight"
    driver.get(globalB.Gdriver)
    k = 1
    height = driver.execute_script(js_height)
    while True:
        if k * 500 < height:
            js_move = "window.scrollTo(0,{})".format(k * 500)
            print(js_move)
            driver.execute_script(js_move)
            time.sleep(0.2)
            height = driver.execute_script(js_height)
            k += 1
        else:
            break
    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(scroll_width+500, scroll_height)

    time.sleep( test_case_time_manager.TIME_SCREENSHOT_WAIT_TIME )
    now = datetime.datetime.now().strftime("%Y%m%d%H%S%M")
    globalB.Gpng = ReadAndWriteFiles().path_screenshotreport()+"\\"+now+'result.png'
    driver.get( globalB.Gdriver )
    time.sleep( test_case_time_manager.TIME_SCREENSHOT_WAIT_TIME )
    driver.get_screenshot_as_file(globalB.Gpng)

if __name__ == "__main__":
    b = reportscreenshot()