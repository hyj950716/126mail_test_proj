# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/15 14:30
@Auth ： 胡英俊(请叫我英俊)
@File ：Home.py
@IDE ：PyCharm
@Motto：Never stop learning
"""
from Util.GetElement import get_element,get_elements
from Util.ParseConfigurationFile import  ParseConfigFile
from selenium import webdriver
import time

from Page.LoginPage import LoginPage

class Home(object):
    def __init__(self,driver):
        self.driver = driver
        self.parse_cf =  ParseConfigFile()
        self.login_page_element_locator_exp_dict = self.parse_cf.get_section_options("home")

    def get_contact_link(self):
       try:
           locator_exp = self.login_page_element_locator_exp_dict["contact_link"]
           contact_link = get_element(self.driver,locator_exp)
           return contact_link
       except Exception as e:
           print("获取页面元素contact_link出现异常！",e)
           raise e
           return None

    def click_contact_link(self):
        contact_link = self.get_contact_link()
        try:
            contact_link.click()
            time.sleep(3)
        except Exception as e:
            print("点击通讯录链接时，出现异常：",e)
            raise e

if __name__ =="__main__":
    driver = webdriver.Chrome(executable_path="e:\\chromedriver.exe")
    driver.get("http://mail.126.com")
    login_page = LoginPage(driver)
    print(login_page.get_frame())
    login_page.switch_to_frame()
    login_page.input_user_name("hxf950716")
    login_page.input_pass_word("Hxf950716!")
    login_page.click_submit_button()

    home = Home(driver)
    home.click_contact_link()
