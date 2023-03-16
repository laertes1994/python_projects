# Read me:
# sample call: python autoTransify.py 97 C:/Users/neil.zhu/1.xlsx
# 脚本 + transify project code + 翻译文件路径
# need to edit the user-data-dir 

import os
 
#需要安装的库
libs = ["selenium","webdriver_manager","pandas","openpyxl"]
 
#循环遍历安装
for lib in libs:
    os.system("pip3 install " + lib)


from optparse import Option
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager import chrome
import pandas as pd
import sys

# 验证现有transify，如果与excel不同，则填充
def operationFill(driver,url,key,translation):
    driver.get(url)
    driver.implicitly_wait(15)
    time.sleep(5)
    elemsearch = driver.find_element(By.CLASS_NAME,'input')
    elemsearch.send_keys(key)
    time.sleep(5)
    elementkey = driver.find_element(By.CSS_SELECTOR,'textarea')
    # elementkey.click()
    # time.sleep(1)
    # elementkey.clear()
    # time.sleep(1)
    # elementkey.send_keys(translation)
    # time.sleep(1)
    # elementsave = driver.find_element(By.CLASS_NAME,'large')
    # elementsave.click()
    # time.sleep(3)
    result = elementkey.get_attribute('value')
    while result != translation:
        elementkey.click()
        time.sleep(1)
        elementkey.clear()
        time.sleep(1)
        elementkey.send_keys(translation)
        time.sleep(1)
        elementsave = driver.find_element(By.CLASS_NAME,'large')
        elementsave.click()
        time.sleep(1)
        result = elementkey.get_attribute('value')
    print('已成功更新 '+ key +' '+ result)



# 读取本地excel
def read_excel_list(path_file_name):
    excel_data = pd.read_excel(path_file_name,engine='openpyxl')
    df_list = excel_data.values.tolist()
    return df_list


# 主方法，读取excel，填充transify
def main(url,path):
    option = webdriver.ChromeOptions()
    chrome_driver_path = "/usr/local/bin/chromedriver"
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


    # option.add_argument(f"--user-data-dir={os.path.expanduser('~')}/Library/Application Support/Google/Chrome")    # 浏览器路径,保存浏览器缓存登录transify
    # option.add_argument(" --profile-directory=Profile 1")
    # option.add_experimental_option('excludeSwitches', ['enable-logging'])
    # option.add_experimental_option("detach",True)
    # option.add_experimental_option("debuggerAddress", "localhost:9222")
    option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(
        executable_path=chrome_driver_path,
        options=option,
    )
    a = read_excel_list(path)
    count = 1
    for i in a: 
       operationFill(driver,url,i[0],i[1])
       print('已成功更新',str(count),'个翻译')
       count=count+1

if __name__ == '__main__':
    a = 'https://transify.sea.com/projects/11/resources/'
    b = str(sys.argv[1])
    # c = '/lang/34'
    url = a+b # 传参拼接url
    print(url)
    # url= "https://transify.sea.com/resources/97/lang/34"
    # url = sys.argv[0]
    file_path = str(sys.argv[2])  # transify路径，格式 key+翻译
    main(url,file_path)
