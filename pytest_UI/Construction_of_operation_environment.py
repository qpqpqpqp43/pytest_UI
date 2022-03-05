'''安装运行环境'''
import os
from pytest_UI.config import root_path
print(rf'set path="{root_path}\allure-2.17.1\bin"')
class Environment_construction(object):
    def __init__(self):
        '''自动化搭建项目运行环境'''
        os.system('pip install pymysql') # pymysql 操作数据库安装
        os.system('pip install -U selenium -i  https://pypi.tuna.tsinghua.edu.cn/simple') # selenium 操作浏览器库安装
        os.system('pip install -U openpyxl') # openpyxl 读Excel文件库
        os.system('pip install pytest -i  https://pypi.tuna.tsinghua.edu.cn/simple') # pytest pytest框架安装
        os.system(rf'set path="{root_path}\allure-2.17.1\bin"') # 修改环境变量,因为是cmd命令,也就是说当关闭此cmd命令行窗口后，将不再起作用,所以还是手工添加环境变量吧
    def cmd_input(self,cmd):
        '''输入自己想要安装的python的pip库'''
        result = os.system(cmd)
        if result == 0:
            print('安装成功!')
        elif result == 1:
            print('安装失败!')

