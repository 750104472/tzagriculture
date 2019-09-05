
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
            inquiryEditPage.save_screen_shot('test_inquiry_50000')
            raise e
        else:
            self.logger.info("测试用例{}测试通过".format(
                self.test_inquiry_50000.__name__))

    @pytest.mark.parametrize('Phone,Date,Note,Budget,expect', inquirydatas.test_inquiry_49000_datas)
    def test_inquiry_49000(self,login_cgr,Phone,Date,Note,Budget,expect):
        """预算总金额不得大于询价项目采购总金额！"""
        inquiryEditPage = login_cgr[1]
        inquiryEditPage.open_url_49000()
        inquiryEditPage.input_message(Phone,Date,Note)
        inquiryEditPage.input_budget(Budget)
        inquiryEditPage.click_publish()
        actual = inquiryEditPage.get_alert_info
        inquiryEditPage.driver_accept_alert()
        try:
            assert expect == actual, '断言失败'
        except AssertionError as e:
            self.logger.info("测试用例{}测试失败\n{}".format(
                self.test_inquiry_49000.__name__,e))
            inquiryEditPage.save_screen_shot('test_inquiry_49000')
            raise e
        else:
            self.logger.info("测试用例{}测试通过".format(
                self.test_inquiry_49000.__name__))

    @pytest.mark.parametrize('Phone,Date,Note,Budget,expect', inquirydatas.test_inquiry_success_datas)
    def test_inquiry_success(self, login_cgr, Phone, Date, Note, Budget, expect):
        """满足限额，询价发布成功！"""
        inquiryEditPage = login_cgr[1]
        inquiryEditPage.open_url_49000()
        inquiryEditPage.input_message(Phone, Date, Note)
        inquiryEditPage.input_budget(Budget)
        inquiryEditPage.click_publish()
        inquiryEditPage.driver_accept_alert()
        actual = inquiryEditPage.get_success_info()
        try:
            assert expect == actual, '断言失败'
        except AssertionError as e:
            self.logger.info("测试用例{}测试失败\n{}".format(
                self.test_inquiry_success.__name__, e))
            inquiryEditPage.save_screen_shot('test_inquiry_success')
            raise e
        else:
            self.logger.info("测试用例{}测试通过".format(
                self.test_inquiry_success.__name__))

    @pytest.mark.parametrize('Phone,Date,Note,Budget,expect', inquirydatas.test_inquiry_fail_datas)
    def test_inquiry_fail(self, login_cgr, Phone, Date, Note, Budget, expect):
        """品目报价权限供应商不足一家时，询价发布失败！"""
        inquiryEditPage = login_cgr[1]
        inquiryEditPage.open_url_fail()
        inquiryEditPage.input_message(Phone, Date, Note)
        inquiryEditPage.input_budget(Budget)
        inquiryEditPage.click_publish()
        actual = inquiryEditPage.get_alert_info
        inquiryEditPage.driver_accept_alert()
        try:
            assert expect == actual, '断言失败'
        except AssertionError as e:
            self.logger.info("测试用例{}测试失败\n{}".format(
                self.test_inquiry_fail.__name__, e))
            inquiryEditPage.save_screen_shot('test_inquiry_fail')
            raise e
        else:
            self.logger.info("测试用例{}测试通过".format(
                self.test_inquiry_fail.__name__))















