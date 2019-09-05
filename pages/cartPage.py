
from pages.base.base import Base
from common.parse_config import ParseConfig
from config.config import LOCATOR_PATH
import pdb

class CartPage(Base):

    locator = ParseConfig(LOCATOR_PATH)

    carturl = locator('TestUrl', 'carturl')
    addproduct_32_20000 = locator('TestUrl', 'addproduct_32_20')
    addproduct_31_20000 = locator('TestUrl', 'addproduct_31_20')
    shopcar_delbuttons = locator('CartPage', 'shopcar_delbuttons')
    compete_button = locator('CartPage', 'compete_button')
    inquiry_button = locator('CartPage', 'inquiry_button')
    order_button = locator('CartPage', 'order_button')

    def open_url(self):
        self.open(self.carturl)

    def open_addproduct_pid_number(self,pid,total_price):
        self.open(f"http://tzagriculture.test.al8l.com/cart/change/{pid}?num={total_price/1000}")
        self.logger.info(f"购物车已添加{total_price/1000}个pid为{pid}商品,总价为{total_price}！")


    def delete_buttons(self):
        is_product = self.is_element_exist(*self.shopcar_delbuttons)
        return is_product

    def get_competebutton_attribute(self):
        ele = self.find_element(*self.compete_button)
        href = ele.get_attribute("href")
        if href == "javascript:void(0)":
            self.logger.info("竞价按钮不可点击！")
            return False
        else:
            self.logger.info("竞价按钮可以点击！")
            return True

    def get_inquirybutton_attribute(self):
        ele = self.find_element(*self.inquiry_button)
        href = ele.get_attribute("href")
        if href == "javascript:void(0)":
            self.logger.info("询价按钮不可点击！")
            return False
        else:
            self.logger.info("询价按钮可以点击！")
            return True

    def get_orderbutton_attribute(self):
        ele = self.find_element(*self.order_button)
        href = ele.get_attribute("href")
        if href == "javascript:void(0)":
            self.logger.info("直购按钮不可点击！")
            return False
        else:
            self.logger.info("直购按钮可以点击！")
            return True

    def delete_products(self):
        try:
            if self.delete_buttons() == False:
                self.logger.info("购物车已清空！")
            else:
                eles = self.find_elements(*self.shopcar_delbuttons)
                for ele in eles:
                    ele.click()
                    self.accept_alert()
                self.logger.info("购物车已清空！")

        except Exception as e:
            self.logger.info("%s"%e)




if __name__ == '__main__':
    pass
