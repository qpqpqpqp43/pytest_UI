'''pytest专用文件,用夹具来传送'''
import os.path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FireFoxService
from pytest_UI.config import root_path
from pytest_UI.config import Browser_object
class Browser(object):
    '''多次实例化只有一个浏览器-> 单例模式运行'''
    __instance = None # 实例一个私有属性的内存空间
    dr = None # 浏览器的driver对象

    def __new__(cls, name='firefox',*args, **kwargs) -> Browser_object:
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)  # 新建一个实例的空间
            if name.lower() == "chrome":
                cls.dr = webdriver.Chrome(service=ChromeService(os.path.join(root_path,"driver/chromedriver.exe")))
            elif name.lower() in ("firefox", "ff"):
                cls.dr = webdriver.Firefox(service=FireFoxService(os.path.join(root_path,"driver/geckodriver.exe")))
            else:
                raise TypeError(f"你选择的浏览器 {name} 不支持！")
            cls.dr.maximize_window() # 浏览器最大化
        return cls.__instance  # __new__ 需要返回一个空间,空间里面有浏览器dr对象

    def close_browser(self):
        if Browser.dr is not None:  # 如果不是None才关闭
            Browser.dr.quit()  # 关闭浏览器的方法
        Browser.dr = None
        Browser.__instance = None

@pytest.fixture
def Browser_objects():
    yield Browser()

if __name__ == '__main__':
    Browser()