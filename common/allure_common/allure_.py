import allure


def allure_title(tytle):
    "allure中显示的用例标题"
    allure.dynamic.title(tytle)


def allure_description(description):
    "allure中显示的用例描述"
    allure.dynamic.description(description)
