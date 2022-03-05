import os
Browser_object = '程序运行返回一个浏览器对象'
root_path = os.path.split( os.path.abspath(__file__) )[0] # 自动获取项目的根目录
Database_config = {'host':'localhost', # 数据库地址
                   'user':'root', # 用户名
                   'password':'123456', # 密码
                   'port':3306, # 端口
                   'db':'woniusales', # 数据库名称
                   'charset':'utf8'} # 数据库配置
if __name__ == '__main__':
    print(root_path)