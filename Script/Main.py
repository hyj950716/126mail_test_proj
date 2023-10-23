# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/15 14:30
@Auth ： 胡英俊(请叫我英俊)
@File ：Main.py
@IDE ：PyCharm
@Motto：Never stop learning
"""
from Util.Excel import Excel
from Config.ProjVar import *
from Action.Action import login,create_contact
from selenium import webdriver
from Util.TimeUtil import  *
import traceback
from Util.Log import *
from Util.TakePic import *

import sys
sys.path.append("E:\\study\\demo\\126mail_test_proj")

def get_test_data(excel_path,sheet_name):
    wb.set_sheet_by_name(sheet_name)
    rows = wb.get_all_rows_values()
    return rows

#print(get_test_data(test_data_file_path,"126账号"))
#print(get_test_data(test_data_file_path,"联系人"))
wb = Excel(test_data_file_path)
user_data = get_test_data(test_data_file_path,"126账号")
contact_data = get_test_data(test_data_file_path,"联系人")
#driver = webdriver.Chrome(executable_path="e:\\chromedriver.exe")
wb.set_sheet_by_name("测试结果")

#第一层循环读取的是登录的测试数据
for line_no in range(1,len(user_data)):
    #print(user)
    user = user_data[line_no]
    flag = user[user_data_if_executed_flag_col_no]
    if "y" not in flag.lower():
        print(user,"被忽略了")
        continue
    else:
        driver = webdriver.Chrome(executable_path="e:\\chromedriver.exe")
        print(user, "需要被执行！")
        user_name = user[user_name_col_no]
        pass_word = user[pass_word_col_no]
        print(user_name,pass_word)
        try:
            login(driver,user_name,pass_word)
            user[user_data_test_result_col_no ]="成功"
            print("用户名：%s 密码：%s 登录成功" %(user_name,pass_word))
            wb.write_line(user_data[0],background_color="DDEEDD")#写了一个表头
            print(user)
            wb.write_line(user)  # 写了测试结果
        except AssertionError as e:
            user[user_data_test_result_col_no] = "失败"
            print("用户名：%s 密码：%s 登录失败" % (user_name, pass_word))
            info("异常的信息：" + str(e))
            info("异常的堆栈信息：" + traceback.format_exc())
            user[user_data_exception_info_col_no] = traceback.format_exc()
            exception_pic_path = take_screenshot(driver)
            info("断言异常时候的截屏路径：%s" % exception_pic_path)
            user[user_data_exception_pic_path_col_no] = exception_pic_path
            continue
        except Exception as e:
            traceback.print_exc()
            user[user_data_test_result_col_no] = "失败"
            print("用户名：%s 密码：%s 登录失败" % (user_name, pass_word))
            info("异常的信息：" + str(e))
            info("异常的堆栈信息：" + traceback.format_exc())
            exception_pic_path = take_screenshot(driver)
            info("测试程序异常时候的截屏路径：%s" %exception_pic_path)
            user[user_data_exception_info_col_no] = traceback.format_exc()
            user[user_data_exception_pic_path_col_no]=exception_pic_path
            continue

        wb.write_line(contact_data[0],background_color="DDEEDD")  # 写了一个表头
        #第二层循环读取的是新建联系人的数据
        for contact_line_no in range(1,len(contact_data)):
            contact  = contact_data[contact_line_no]
            if "y" not in contact[contact_data_if_executed_flag_col_no].lower():
                print(contact, "被忽略了")
                continue
            else:
                print(contact,"要被执行了。")

                name = contact[name_col_no]
                email = contact[email_col_no]
                mobile = contact[mobile_col_no]
                star = contact[star_col_no]
                other_info = contact[other_info_col_no]
                assert_word = contact[assert_word_col_no]
                print(name,email,mobile,star,other_info,assert_word)
                if name is None:
                    name = ""
                if email is None:
                    email=""
                if mobile is None:
                    mobile=""
                if star is None:
                    star = "否"
                if other_info is None:
                    other_info =""
                contact[test_time_col_no] = get_date_time()
                try:
                    create_contact(driver,name,email,mobile,star,other_info,assert_word)
                    contact[contact_test_result_col_no]="成功"
                    print("%s 联系人创建成功"  %name)
                except Exception as e:
                    contact[contact_test_result_col_no] = "失败"
                    print("%s 联系人创建失败" %"失败")
                    info("异常的信息："+ str(e))
                    info("异常的堆栈信息："+traceback.format_exc())
                    exception_pic_path = take_screenshot(driver)
                    info("断言异常时候的截屏路径：%s" % exception_pic_path)
                    contact[contact_exception_info_col_no]=traceback.format_exc()
                    contact[contact_exception_pic_path_col_no]=exception_pic_path
                wb.write_line(contact)  # 写了测试结果

        driver.close()