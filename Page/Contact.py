# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/15 14:30
@Auth ： 胡英俊(请叫我英俊)
@File ：Contact.py
@IDE ：PyCharm
@Motto：Never stop learning
"""
from Util.GetElement import get_element,get_elements
from Util.ParseConfigurationFile import  ParseConfigFile
from selenium import webdriver
import time

from Page.LoginPage import LoginPage
from Page.Home import Home

class Contact(object):
    def __init__(self,driver):
        self.driver = driver
        self.parse_cf =  ParseConfigFile()
        self.login_page_element_locator_exp_dict = self.parse_cf.get_section_options("contact")

    def get_add_new_contact_button(self):
       try:
           locator_exp = self.login_page_element_locator_exp_dict["add_new_contact"]
           add_new_contact_button = get_element(self.driver,locator_exp)
           return add_new_contact_button
       except Exception as e:
           print("获取页面元素 add_new_contact_button 出现异常！",e)
           raise e
           return None

    def click_add_new_contact_button(self):
        add_new_contact_button = self.get_add_new_contact_button()
        try:
            add_new_contact_button.click()
            time.sleep(2)
        except Exception as e:
            raise e
            print("点击通讯录链接时，出现异常：",e)

    def get_name(self):
       try:
           locator_exp = self.login_page_element_locator_exp_dict["name_input_box"]
           name_input_box = get_element(self.driver,locator_exp)
           return name_input_box
       except Exception as e:
           print("获取页面元素name_input_box出现异常！",e)
           raise e
           return None

    def input_name(self,name):
        name_input_box = self.get_name()
        try:
            name_input_box.send_keys(name)
        except Exception as e:
            print("name输入框输入框输入时，出现异常：",e)
            raise e

    def get_email(self):
       try:
           locator_exp = self.login_page_element_locator_exp_dict["email_input_box"]
           email_input_box = get_element(self.driver,locator_exp)
           return email_input_box
       except Exception as e:
           print("获取页面元素 email_input_box 出现异常！",e)
           raise e
           return None

    def input_email(self,email):
        email_input_box = self.get_email()
        try:
            email_input_box.send_keys(email)
        except Exception as e:
            print("email 输入框输入框输入时，出现异常：",e)
            raise e

    def get_star_contact(self):
        try:
            locator_exp = self.login_page_element_locator_exp_dict["star_contact"]
            star_contact = get_element(self.driver, locator_exp)
            return star_contact
        except Exception as e:
            print("获取页面元素 star_contact 出现异常！", e)
            raise e
            return None

    def click_star_contact(self):
        star_contact = self.get_star_contact()
        try:
            star_contact.click()
        except Exception as e:
            print("点击 star_contact 时，出现异常：",e)
            raise e

    def get_mobile(self):
        try:
            locator_exp = self.login_page_element_locator_exp_dict["mobile_input_box"]
            mobile_input_box = get_element(self.driver,locator_exp)
            return mobile_input_box
        except Exception as e:
            print("获取页面元素 mobile_input_box 出现异常！",e)
            raise e
            return None

    def input_mobile(self,mobile):
        mobile_input_box = self.get_mobile()
        try:
            mobile_input_box.send_keys(mobile)
        except Exception as e:
            print("mobile 输入框输入框输入时，出现异常：",e)
            raise e

    def get_other_info(self):
        try:
            locator_exp = self.login_page_element_locator_exp_dict["other_info_input_box"]
            other_info_input_box = get_element(self.driver,locator_exp)
            return other_info_input_box
        except Exception as e:
            print("获取页面元素 other_info_input_box 出现异常！",e)
            raise e
            return None

    def input_other_info(self,info):
        other_info_input_box =  self.get_other_info()
        try:
            other_info_input_box.send_keys(info)
        except Exception as e:
            print("_other_info 输入框输入框输入时，出现异常：",e)
            raise e

    def get_submit_button(self):
        try:
            locator_exp = self.login_page_element_locator_exp_dict["submit_button"]
            submit_button = get_element(self.driver,locator_exp)
            return submit_button
        except Exception as e:
            print("获取页面元素 submit_button 出现异常！",e)
            raise e
            return None

    def click_submit_button(self):
        submit_button = self.get_submit_button()
        try:
            submit_button.click()
            time.sleep(3)
        except Exception as e:
            print("submit_button 按钮点击时，出现异常：",e)
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

    contact = Contact(driver)
    contact.click_add_new_contact_button()

    contact.input_name("吴老师")
    contact.input_email("39837383@125.com")
    contact.click_star_contact()

    contact.input_mobile("12948383828")
    contact.input_other_info("天气不错！")

    contact.click_submit_button()
