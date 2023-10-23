# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/15 14:30
@Auth ： 胡英俊(请叫我英俊)
@File ：LoginPage.py
@IDE ：PyCharm
@Motto：Never stop learning
"""
from Util.GetElement import get_element,get_elements
from Util.ParseConfigurationFile import  ParseConfigFile
from selenium import webdriver
import time

class LoginPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parse_cf =  ParseConfigFile()
        self.login_page_element_locator_exp_dict = self.parse_cf.get_section_options("login")


    def get_frame(self):
       try:
           locator_exp = self.login_page_element_locator_exp_dict["frame"]
           frame = get_element(self.driver,locator_exp)
           return frame
       except Exception as e:
           print("获取页面元素frame出现异常！",e)
           raise e
           return None

    def switch_to_frame(self):
        frame = self.get_frame()
        if frame:
            self.driver.switch_to.frame(frame)
        else:
            print("切入frame失败！frame对象是%s"  %frame)
            raise e

    def get_user_name(self):
       try:
           locator_exp = self.login_page_element_locator_exp_dict["user_name"]
           user_name = get_element(self.driver,locator_exp)
           return user_name
       except Exception as e:
           print("获取页面元素user_name出现异常！",e)
           raise e
           return None

    def input_user_name(self,user_name):
        user_name_inputbox = self.get_user_name()
        try:
            user_name_inputbox.send_keys(user_name)
        except Exception as e:
            print("用户名输入框输入时，出现异常：",e)
            raise e

    def get_pass_word(self):
       try:
           locator_exp = self.login_page_element_locator_exp_dict["pass_word"]
           pass_word = get_element(self.driver,locator_exp)
           return pass_word
       except Exception as e:
           print("获取页面元素pass_word出现异常！",e)
           raise e
           return None

    def input_pass_word(self,pass_word):
        pass_word_inputbox = self.get_pass_word()
        try:
            pass_word_inputbox.send_keys(pass_word)
        except Exception as e:
            print("密码输入框输入时，出现异常：",e)
            raise e

    def get_submit_button(self):
       try:
           locator_exp = self.login_page_element_locator_exp_dict["submit_button"]
           submit_button = get_element(self.driver,locator_exp)
           return submit_button
       except Exception as e:
           print("获取页面元素submit_button出现异常！",e)
           raise e
           return None

    def click_submit_button(self):
        submit_button = self.get_submit_button()
        try:
            submit_button.click()
            time.sleep(3)
        except Exception as e:
            print("点击登录按钮时，出现异常：",e)
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


