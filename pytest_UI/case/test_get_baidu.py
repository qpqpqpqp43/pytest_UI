'''测试打开百度,输入测试，并点击搜索'''
import time


def test_baidu(Browser_objects):
    from pytest_UI.common.beautiful_allure import allure_report
    Browser_objects.dr.implicitly_wait(10) # 设置隐式等待
    allure_object = allure_report(Priority='blocker',Functional_modules='搜索功能',title='打开百度搜索测试',browser=Browser_objects.dr)
    Browser_objects.dr.get('http://www.baidu.com')
    allure_object.Document_use_cases(data='http://www.baidu.com',name='打开百度')
    Browser_objects.dr.find_element('xpath','//*[@id="kw"]').send_keys('测试')
    allure_object.Document_use_cases(data='测试',name='输入搜索内容')
    Browser_objects.dr.find_element('xpath','//*[@id="su"]').click()
    allure_object.Document_use_cases(data='',name='点击搜索')
    time.sleep(3) # 等浏览器跳转,如果浏览器跳转过慢,可以设置长点
    allure_object.allure_Screenshots() # 截图