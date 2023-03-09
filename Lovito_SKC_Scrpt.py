import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementExceptionc
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import csv

# url='https://e-procurement.shopee.com/frs/product/skc-detail/'


def get_url_list():
    excel_data = pd.read_csv("test1.csv")
    df_list = excel_data.values.tolist()
    full_url_list = []
    for i in df_list:
      url_prefix = 'https://e-procurement.shopee.com/frs/product/skc-detail/'
      full_url_list.append(url_prefix+i[0])
    print(full_url_list)
    return full_url_list

def get_product_data(full_url,browser):
    html = browser.page_source
    bs = BeautifulSoup(html, 'html.parser')
    taglist = bs.findAll("span",class_="td-content td-content-ellipsis")
    listA = []
    listA.append(full_url)
    for j in taglist:
          if(len(j.get_text(strip=True))>4):
          #   print(i.get_text(strip=True))
              listA.append((j.get_text(strip=True)))
        # print(listA)
    return listA

def iselement(browser):
    try:
        browser.find_element(By.CLASS_NAME,"login")
        return True
    except NoSuchElementException:
        return False


def main():
    fullList = []
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver =  "/usr/local/bin/chromedriver"
    browser1 = webdriver.Chrome(executable_path=chrome_driver, options=options)
    browser1.find_elements
    product_list = get_url_list()
    for i in product_list:
        browser1.get(i)
        time.sleep(5)
        if iselement(browser1):
            browser1.find_element(By.XPATH,"//*[@id='app']/div/div[1]/div/div[2]/div[2]/button[2]/span").click()
            time.sleep(10)
            fullList.append(get_product_data(i,browser1))
        else:
            fullList.append(get_product_data(i,browser1))
        print(fullList)
    with open('results.csv', 'w', newline='') as result_file:
        writer = csv.writer(result_file)
        writer.writerows(fullList)

if __name__ == '__main__':
    main()
 