import os

from save_report_history.save_report_history import Get_History


# utf-8

class GetReport:
    def get_report(self):
        # 1 、 生成json文件
        print("正在生成JSON文件".center(76, '-'))
        # cmd = r"pytest D:\PycharmProjects\ApiTest\main.py " \
        cmd = r"D: && cd D:\PycharmProjects\ApiTest && pytest --alluredir=D:\PycharmProjects\ApiTest\reports\allure  --clean-alluredir "

        os.system(cmd)

        print("正在复制配置信息文件".center(76, '-'))

        # 2、 复制配置文件到json文件中
        # cmd1 = r'D: && cd D:\PycharmProjects\ApiTest\alluer-environment && copy /y environment.properties D:\PycharmProjects\ApiTest\reports\allure\environment.properties'
        cmd1 = r'D: ; cd D:\PycharmProjects\ApiTest\alluer-environment ; copy /y environment.properties D:\PycharmProjects\ApiTest\reports\allure\environment.properties'
        os.system(cmd1)

        print("正在生成报告".center(76, '-'))
        # 3、生成报告
        cmd2 = r"allure generate D:\PycharmProjects\ApiTest\reports\allure -o D:\PycharmProjects\ApiTest\reports\report --clean "
        os.system(cmd2)
        print("报告生成完毕！！！！".center(76, '-'))

        # 4、 替换历史记录文件
        print("正在生成历史趋势文件".center(76, '-'))
        Get_History().get_history()

    # 5、为报告开启端口，共享查看
    # print('正在开启端口，分享报告')
    # cmd3 = r'allure open -h 192.168.81.102 -p 8885 C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\reports'
    # os.system(cmd3)


if __name__ == '__main__':
    # gt = GetReport()
    GetReport().get_report()
