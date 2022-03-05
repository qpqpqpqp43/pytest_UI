import pytest
import subprocess
#1.生成测试的数据
allure_result="./report/allure_result" #存放结果数据的
allure_html="./report/allure_html"#存放html报告的
pytest.main(["case","-v","-s",f"--alluredir={allure_result}","--clean-alluredir"])
#2.调用命令生成报告
subprocess.run(f"allure generate {allure_result} -o {allure_html} --clean",shell=True,universal_newlines=True) #阻塞式的，等待报告生成

