
import pytest
from common.record_log import logger
from datas.cart_datas import CartData
import pdb


class TestCart(object):
    """询价项目功能点测试"""
    logger = logger
    cartdata = CartData

    @pytest.mark.parametrize('pid,total_price,compete_attribute,inquiry_attribute,order_attribute', cartdata.test_cart_one_noservice_product_datas)
    def test_cart_one_noservice_product(self,login_cgr,pid,total_price,compete_attribute,inquiry_attribute,order_attribute):
        """单个非农机服务商品加入购物车，判断不同采购金额对应的竞价、询价和直购按钮状态是否符合预期"""
        cate_page = login_cgr[2]
        cate_page.open_addproduct_pid_number(int(pid),int(total_price))
        actual_compete_attribute = cate_page.get_competebutton_attribute()
        actual_inquiry_attribute = cate_page.get_inquirybutton_attribute()
        actual_order_attribute = cate_page.get_orderbutton_attribute()
        try:
            assert actual_compete_attribute == compete_attribute, '竞价按钮状态不符合预期'
            assert actual_inquiry_attribute == inquiry_attribute, '询价按钮状态不符合预期'
            assert actual_order_attribute == order_attribute, '直购按钮状态不符合预期'
        except AssertionError as e:
            self.logger.info("测试用例{}测试失败\n{}".format(
                self.test_cart_one_noservice_product.__name__,e))
            cate_page.save_screen_shot('test_cart_one_noservice_product')
            raise e
        else:
            self.logger.info("测试用例{}测试通过".format(
                self.test_cart_one_noservice_product.__name__))

    @pytest.mark.parametrize('pid1, total_price1, pid2, total_price2,pid3, total_price3,compete_attribute, inquiry_attribute,order_attribute',cartdata.test_cart_three_noservice_product_datas)
    def test_cart_three_noservice_product(self, login_cgr, pid1, total_price1, pid2, total_price2,pid3, total_price3,compete_attribute, inquiry_attribute,order_attribute):
        """单个非农机服务商品加入购物车，判断不同采购金额对应的竞价、询价和直购按钮状态是否符合预期"""
        cate_page = login_cgr[2]
        cate_page.open_addproduct_pid_number(int(pid1), int(total_price1))
        cate_page.open_addproduct_pid_number(int(pid2), int(total_price2))
        cate_page.open_addproduct_pid_number(int(pid3), int(total_price3))
        actual_compete_attribute = cate_page.get_competebutton_attribute()
        actual_inquiry_attribute = cate_page.get_inquirybutton_attribute()
        actual_order_attribute = cate_page.get_orderbutton_attribute()
        try:
            assert actual_compete_attribute == compete_attribute, '竞价按钮状态不符合预期'
            assert actual_inquiry_attribute == inquiry_attribute, '询价按钮状态不符合预期'
            assert actual_order_attribute == order_attribute, '直购按钮状态不符合预期'
        except AssertionError as e:
            self.logger.info("测试用例{}测试失败\n{}".format(
                self.test_cart_one_noservice_product.__name__, e))
            cate_page.save_screen_shot('test_cart_one_noservice_product')
            raise e
        else:
            self.logger.info("测试用例{}测试通过".format(
                self.test_cart_one_noservice_product.__name__))















