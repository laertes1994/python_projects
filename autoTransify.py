from optparse import Option
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import sys

def operationFill(url,key,translation):
    option = webdriver.ChromeOptions()
    option.add_argument("user-data-dir=C:/Users/neil.zhu/Selenium_Data")    # 浏览器路径
    # option.add_experimental_option("detach",True)
    # url = "https://transify.sea.com/resources/360/lang/34"
    driver = webdriver.Chrome(options=option)  
    driver.get(url)
    time.sleep(8)
    elemsearch = driver.find_element(By.CLASS_NAME,'input')
    elemsearch.send_keys(key)
    time.sleep(3)
    elementkey = driver.find_element(By.CSS_SELECTOR,'textarea')
    elementkey.click()
    elementkey.clear()
    elementkey.send_keys(translation)
    time.sleep(1)
    elementsave = driver.find_element(By.CLASS_NAME,'large')
    elementsave.click()
    time.sleep(3)

def read_excel_list(path_file_name):
    excel_data = pd.read_excel(path_file_name,engine='openpyxl')
    df_list = excel_data.values.tolist()
    return df_list

def main(url,path):
    a = read_excel_list(path)
    count = 1
    for i in a: 
       operationFill(url,i[0],i[1])
       print(count)
       count=count+1

if __name__ == '__main__':
    url= "https://transify.sea.com/resources/97/lang/34"
    # url = sys.argv[0]
    # file_path = sys.argv[1]
    file_path = 'C:/Users/neil.zhu/1.xlsx'
    main(url,file_path)


# url = "https://transify.sea.com/resources/360/lang/34"
# a = read_excel_list('C:/Users/neil.zhu/test.xlsx')
# for i in a:
#     operationFill(url,i[0],i[1])