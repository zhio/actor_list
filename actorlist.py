from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from lxml import etree
import os
def get_actor_name():
    browser = webdriver.Chrome()
    try:
        browser.get('https://www.baidu.com')
        currentWin = browser.current_window_handle
        input = browser.find_element_by_id('kw')
        input.send_keys('中国演员')
        input.send_keys(Keys.ENTER)
        time.sleep(5)
        handles = browser.window_handles
        for i in handles:
            if currentWin == i:
                continue
            else:
                # 将driver与新的页面绑定起来
                driver = driver.switch_to_window(i)
        i = 0
        actor_name = []
        try:
            while i < 221100:
                i = i+1
                html=browser.page_source
                html=etree.HTML(html)
                name = html.xpath('//div[@class="op_exactqa_itemsArea c-row "]//p[@class="c-gap-top-small"]/a/@title')
                print(name)
                with open("China_actor", "a") as f:
                    f.write(str(name)+"\n")
                actor_name.extend(name)
                next_ = browser.find_element_by_xpath('//span[@class="opui-page-next OP_LOG_BTN"]').click()
                time.sleep(0.5)
        except:
            print("结束")
            time.sleep(15)
    finally:
        browser.close()

    return 0

get_actor_name()
