
import pytest
from datas.login_datas import LoginData
from common.record_log import logger
import pdb


class TestLogin(object):
    """登录测试用例"""
    logger = logger
    t_data = LoginData

    @pytest.mark.login
    @pytest.mark.parametrize('user, pwd, expect', t_data.login_success_data)
    def test_login_success(self, open_url, user, pwd, expect):
        """登录:登录成功"""
        login_page = open_url
        login_page.login(user, pwd)
        actual = login_page.get_login_success_info
        try:
            assert expect == actual, '断言失败'
        except AssertionError as e:
            self.logger.info("测试用例{}-{}-{}测试失败\n{}".format(
                self.test_login_success.__name__,
                user,
                pwd,
                e))
            login_page.save_screen_shot('login_fail')
            raise e
        else:
            self.logger.info("测试用例{}-{}-{}测试通过".format(
                self.test_login_success.__name__,
                user,
                pwd))



if __name__ == '__main__':
    pytest.main()
