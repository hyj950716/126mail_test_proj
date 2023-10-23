# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/15 14:30
@Auth ： 胡英俊(请叫我英俊)
@File ：ProjVar.py
@IDE ：PyCharm
@Motto：Never stop learning
"""
import os

#print(__file__)#获得文件当前的绝对路径
#print(os.path.dirname(__file__))

#获取当前工程所在的目录
proj_path = os.path.dirname(os.path.dirname(__file__))

#获取日志配置文件的所在路径
log_config_path = os.path.join(proj_path,"Config\\Logger.conf")

#页面元素定位表达式配置文件的所在路径
page_element_locator_file_path =  os.path.join(proj_path,"Config\\PageElementLocator.ini")

#获取excel数据文件的路径
test_data_file_path = os.path.join(proj_path,"Data\\126邮箱联系人.xlsx")

user_data_if_executed_flag_col_no = 4
user_name_col_no = 1
pass_word_col_no = 2
user_data_test_result_col_no = 5

name_col_no=1
email_col_no=2
star_col_no=3
mobile_col_no = 4
other_info_col_no=5
assert_word_col_no = 6
contact_data_if_executed_flag_col_no=7
test_time_col_no = 8
contact_test_result_col_no = 9
contact_exception_info_col_no = 10
user_data_exception_info_col_no = 6
user_data_exception_pic_path_col_no = 7
contact_exception_pic_path_col_no =11



if __name__ == "__main__":
    print(proj_path )
    print(log_config_path)
    print(page_element_locator_file_path )
    print(test_data_file_path )
