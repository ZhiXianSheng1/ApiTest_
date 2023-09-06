import os

import pytest
from common import allure_main
from common.allure_main import GetReport
from save_report_history.save_report_history import Get_History

if __name__ == '__main__':
    # print("正在生成JSON文件".center(76, '-'))
    # # cmd = r"pytest D:\PycharmProjects\ApiTest\main.py "
    # cmd = r"D: && cd D:\PycharmProjects\ApiTest && pytest --alluredir=D:\PycharmProjects\ApiTest\reports\allure  --clean-alluredir "
    #
    # os.system(cmd)
    #
    # print("正在复制配置信息文件".center(76, '-'))
    # # 2、 复制配置文件到json文件中
    # cmd1 = r'D: ; cd D:\PycharmProjects\ApiTest\alluer-environment ; copy /y environment.properties D:\PycharmProjects\ApiTest\reports\allure\environment.properties'
    # os.system(cmd1)
    #
    # print("正在生成报告".center(76, '-'))
    # # 3、生成报告
    # cmd2 = r"allure generate D:\PycharmProjects\ApiTest\reports\allure -o D:\PycharmProjects\ApiTest\reports\report --clean "
    # os.system(cmd2)
    # print("报告生成完毕！！！！".center(76, '-'))
    #
    # # 4、 替换历史记录文件
    # print("正在生成历史趋势文件".center(76, '-'))
    # Get_History().get_history()

    get = GetReport()
    get.get_report()
    # print(os.getcwd())
    # pytest.main()
