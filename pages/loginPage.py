
from pages.base.base import Base
from common.parse_config import ParseConfig
from config.config import LOCATOR_PATH

class LoginPage(Base):

    locator = ParseConfig(LOCATOR_PATH)

    url = locator('TestUrl', 'url')
    username_input = locator('LoginPage', 'username_input')  # 用户名输入框 实际：username_input = ('id', 'user_login')
    password_input = locator('LoginPage', 'password_input')  # 密码输入框
    login_button = locator('LoginPage', 'login_button')  # 登录按钮
    login_success_info = locator('LoginPage', 'login_success_info')

    def login(self, phone: str, password: str):
        self.logger.info("开始登录")
        self.input_user(phone)
        self.input_password(password)
        self.click_login()

    def open_url(self):
        self.open(self.url)

    def input_user(self, phone: str):
        self.logger.info("输入用户名:{}".format(phone))
        self.send_keys(*self.username_input, value=phone)

    def input_password(self, password: str):
        self.logger.info("输入密码:{}".format(password))
        self.send_keys(*self.password_input, value=password)

    def click_login(self):
        self.logger.info("点击登录按钮")
        self.click(*self.login_button)

    @property
    def get_login_success_info(self):
        value = self.get_element_text(*self.login_success_info)
        self.logger.info("获取登录成功断言信息:{}".format(value))
        return value




if __name__ == '__main__':
    pass
