import os

import pytest
from common import allure_main
from common.allure_main import GetReport
from save_report_history.save_report_history import Get_History

if __name__ == '__main__':

    get = GetReport()
    get.get_report()
