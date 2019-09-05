
import pytest
from datetime import datetime
from pages.loginPage import LoginPage
from pages.inquiryEditPage import InquiryEditPage
from pages.cartPage import CartPage
from selenium import webdriver
from py._xmlgen import html
from common.record_log import logger

_driver = None
_driver_type = "chrome"


# 测试失败时添加截图和测试用例描述(用例的注释信息)
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    cells.pop(2)


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop(2)


def _capture_screenshot():
    """
    截图保存为base64
    :return:
    """
    return _driver.get_screenshot_as_base64()

@pytest.fixture(scope='session')
def driver():
    global _driver
    global _driver_type
    if _driver_type=="chrome":
        logger.info('------------open browser------------')
        _driver = webdriver.Chrome()
        # _driver.maximize_window()
    else:
        logger.info('------------open browser------------')
        _driver = webdriver.Firefox()
    yield _driver
    logger.info('------------close browser------------')
    _driver.quit()

@pytest.fixture(scope='class')
def ini_pages(driver):
    login_page = LoginPage(driver)
    inquiryEditPage = InquiryEditPage(driver)
    cart_page = CartPage(driver)
    yield driver, login_page,inquiryEditPage,cart_page

# test_login.py调用
@pytest.fixture(scope='function')
def open_url(ini_pages):
    driver = ini_pages[0]
    login_page = ini_pages[1]
    login_page.open_url()
    yield login_page
    driver.delete_all_cookies()


# test_login.py调用
@pytest.fixture(scope='function')
def login_cgr(ini_pages):
    driver, login_page, inquiryEditPage,cart_page= ini_pages
    login_page.open_url()
    login_page.login("tz_cgr","12345678")
    yield login_page,inquiryEditPage,cart_page
    driver.delete_all_cookies()
#
#
# @pytest.fixture(scope='function')
# def login_cgr(ini_pages):
#     driver, login_page, modelplates_page,newproject_page= ini_pages
#     login_page.open_url()
#     login_page.login(NewprojectData.user_password['username'],
#                      NewprojectData.user_password['password'])
#
#     yield login_page,modelplates_page,newproject_page
#     driver.delete_all_cookies()




