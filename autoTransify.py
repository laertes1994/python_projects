# Read me:
# sample call: python autoTransify.py 97 C:/Users/neil.zhu/1.xlsx
# 脚本 + transify project code + 翻译文件路径
# need to edit the user-data-dir 
# need to install python + selenium + webdriver_manager + chrome driver + pandas + openpyxl

import os
 
#需要安装的库
libs = ["selenium","webdriver_manager","pandas","openpyxl"]
 
#循环遍历安装
for lib in libs:
    os.system("pip install " + lib)


from optparse import Option
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import pandas as pd
import sys


def operationFill(url,key,translation):
    option = webdriver.EdgeOptions()
    option.add_argument("user-data-dir=C:/Users/neil.zhu/AppData/Local/Microsoft/Edge/User Data")    # 浏览器路径,保存浏览器缓存登录transify
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    # option.add_experimental_option("detach",True)
    driver = webdriver.Edge(EdgeChromiumDriverManager().install(),options=option)  
    driver.get(url)
    # time.sleep(8)
    driver.implicitly_wait(10)
    elemsearch = driver.find_element(By.CLASS_NAME,'input')
    elemsearch.send_keys(key)
    time.sleep(3)
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
        time.sleep(3)
        result = elementkey.get_attribute('value')
        
    print('已成功更新 '+ key +' '+ translation)

def read_excel_list(path_file_name):
    excel_data = pd.read_excel(path_file_name,engine='openpyxl')
    df_list = excel_data.values.tolist()
    return df_list

def main(url,path):
    a = read_excel_list(path)
    count = 1
    for i in a: 
       operationFill(url,i[0],i[1])
       print('已成功更新',str(count),'个翻译')
       count=count+1

if __name__ == '__main__':
    a = 'https://transify.sea.com/resources/'
    b = str(sys.argv[1])
    c = '/lang/34'
    url = a+b+c # 传参拼接url
    print(url)
    # url= "https://transify.sea.com/resources/97/lang/34"
    # url = sys.argv[0]
    file_path = str(sys.argv[2])  # transify路径，格式 key+翻译
    main(url,file_path)


# url = "https://transify.sea.com/resources/360/lang/34"
# a = read_excel_list('C:/Users/neil.zhu/test.xlsx')
# for i in a:
#     operationFill(url,i[0],i[1])