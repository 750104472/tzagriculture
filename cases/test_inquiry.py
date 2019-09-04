
import pytest
from common.record_log import logger
from datas.inquiry_datas import InquiryData
from pages.inquiryEditPage import InquiryEditPage
import pdb


class TestInquiry(object):
    """询价项目功能点测试"""
    logger = logger
    inquirydatas = InquiryData

    @pytest.mark.parametrize('Phone,Date,Note,Budget,expect',inquirydatas.test_inquiry_50000_datas)
    def test_inquiry_50000(self,login_cgr,Phone,Date,Note,Budget,expect):
        """询价项目采购总金额需要小于5万元！"""
        inquiryEditPage = login_cgr[1]
        inquiryEditPage.open_url_50000()
        inquiryEditPage.input_message(Phone,Date,Note)
        inquiryEditPage.input_budget(Budget)
        inquiryEditPage.click_publish()
        actual = inquiryEditPage.get_alert_info
        inquiryEditPage.driver_accept_alert()
        try:
            assert expect == actual, '断言失败'
        except AssertionError as e:
            self.logger.info("测试用例{}测试失败\n{}".format(
                self.test_inquiry_50000.__name__,e))
            inquiryEditPage.save_screen_shot('login_fail')
            raise e
        else:
            self.logger.info("测试用例{}测试通过".format(
                self.test_inquiry_50000.__name__))














