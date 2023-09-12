import os

from save_report_history.save_report_history import Get_History

class GetReport:
    def get_report(self):
        current = os.path.abspath(__file__)  # 当前路径
        # print(current)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(current)))  # 基础路径
        path1 = BASE_DIR + os.sep + r"reports\allure"
        path2 = BASE_DIR + os.sep + "alluer-environment"
        path3 = BASE_DIR + os.sep + r"reports\allure\environment.properties"
        path4 = BASE_DIR + os.sep + r"reports\report"

        # 1 、 生成json文件
        print("正在生成JSON文件".center(76, '-'))
        cmd = rf"D: && cd {BASE_DIR} && pytest --alluredir={path1} --clean-alluredir "
        os.system(cmd)
        print("正在复制配置信息文件".center(76, '-'))

        # 2、 复制配置文件到json文件中
        cmd1 = rf'D: ; cd {path2} ; copy /y environment.properties {path3}'
        os.system(cmd1)
        print("正在生成报告".center(76, '-'))

        # 3、生成报告
        cmd2 = fr"allure generate {path1} -o {path4} --clean "
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
    GetReport().get_report()