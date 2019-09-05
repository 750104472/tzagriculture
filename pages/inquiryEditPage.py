
from pages.base.base import Base
from common.parse_config import ParseConfig
from config.config import LOCATOR_PATH

class InquiryEditPage(Base):

    # ;询价项目采购总金额需要小于5万元！
    # ;预算总金额不得大于询价项目采购总金额！
    locator = ParseConfig(LOCATOR_PATH)
    inquiry_url_50000 = locator('TestUrl', 'inquiry_url_50000')
    inquiry_url_49000 = locator('TestUrl', 'inquiry_url_49000')
    inquiry_url_fail = locator('TestUrl', 'inquiry_url_fail')
    phone = locator('InquiryPage', 'phone')
    date = locator('InquiryPage', 'date')
    pay = locator('InquiryPage', 'pay')
    budget = locator('InquiryPage', 'budget')
    note = locator('InquiryPage', 'note')
    publish = locator('InquiryPage', 'publish')
    success_info = locator('InquiryPage', 'success_info')

    def open_url_50000(self):
        self.logger.info("----进入询价页面,询价项目总价为50000元！----")
        self.open(self.inquiry_url_50000)

    def open_url_49000(self):
        self.logger.info("----进入询价页面,询价项目总价为49000元！----")
        self.open(self.inquiry_url_49000)

    def open_url_fail(self):
        self.logger.info("----进入询价页面,询价项目总价为49000元,可报价供应商不足1家！----")
        self.open(self.inquiry_url_fail)

    def input_message(self,Phone,Date,Note):
        self.logger.info("输入联系手机、收货日期、产品要求、支付方式")
        self.send_keys(*self.phone,Phone)
        self.send_keys(*self.date,Date)
        self.send_keys(*self.note,Note)
        self.click(*self.pay)

    def input_budget(self,Budget):
        self.logger.info(f"输入预算总金额：{Budget}")
        self.send_keys(*self.budget,Budget)

    def click_publish(self):
        self.logger.info("点击发布按钮")
        self.click(*self.publish)

    @property
    def get_alert_info(self):
        value = self.get_alert_text
        self.logger.info("弹框提示文字为:{}".format(value))
        return value

    def get_success_info(self):
        value = self.get_element_text(*self.success_info)
        self.logger.info("询价发布成功提示信息为:{}".format(value))
        return value

    def driver_accept_alert(self):
        self.accept_alert()
        self.logger.info("Alert弹框已确认！")



if __name__ == '__main__':
    pass
