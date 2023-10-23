# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/15 14:30
@Auth ： 胡英俊(请叫我英俊)
@File ：Action.py
@IDE ：PyCharm
@Motto：Never stop learning
"""
from selenium import webdriver
from Page.LoginPage import LoginPage
from Page.Home import Home
from Page.Contact import Contact
import time
import sys
from Config import ProjVar

#sys.path.append(os.path.join(ProjVar,"Page"))

def login(driver,user_name,pass_word):
    driver.get("http://mail.126.com")
    login_page = LoginPage(driver)
    print(login_page.get_frame())
    login_page.switch_to_frame()
    login_page.input_user_name(user_name)
    login_page.input_pass_word(pass_word)
    login_page.click_submit_button()
    time.sleep(3)
    assert "收件箱" in driver.page_source

def create_contact(driver,name,email,mobile,star,info,assert_word):
    #login(driver, user_name, pass_word)
    home = Home(driver)
    home.click_contact_link()

    contact = Contact(driver)
    contact.click_add_new_contact_button()

    contact.input_name(name)
    contact.input_email(email)
    if "是" in star:
        contact.click_star_contact()
    contact.input_mobile(mobile)
    contact.input_other_info(info)
    contact.click_submit_button()
    time.sleep(1)
    assert assert_word in driver.page_source

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="e:\\chromedriver.exe")
    #login(driver,"testman1980","wulaoshi1978")
    try:
        create_contact(driver,"hxf950716","Hxf950716!","wulaoshi",
                   "ieufuf@qq.com","13493838383","True","天气不错！")
        print("用例执行成功了！")
    except Exception as e:
        print(e)
        print("用例执行失败")