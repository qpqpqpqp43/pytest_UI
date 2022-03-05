'''写allure报告'''
import allure
BLOCKER = 'blocker'       # blocker：阻塞缺陷（功能未实现，无法下一步）
CRITICAL = 'critical'     # critical：严重缺陷（功能点缺失）
NORMAL = 'normal'         # normal： 一般缺陷（边界情况，格式错误）
MINOR = 'minor'           # minor：次要缺陷（界面错误与ui需求不符）
TRIVIAL = 'trivial'       # trivial： 轻微缺陷（必须项无提示，或者提示不规范）

class allure_report(object):
    def __init__(self,Priority,Functional_modules,title,browser):
        import allure
        allure.dynamic.severity(Priority) # 优先级
        allure.dynamic.feature(Functional_modules) # 功能模块
        allure.dynamic.title(title) # 标题
        self.browser = browser
    def Document_use_cases(self,data,name):
        '''
        :param data: 测试步骤
        :param name: 用例名称
        :return:
        '''
        allure.attach(body=data,name=name,attachment_type=allure.attachment_type.CSV)

    def allure_Screenshots(self):
        '''截图'''
        allure.attach(body=self.browser.get_screenshot_as_png(), name='截图',
                      attachment_type=allure.attachment_type.PNG)