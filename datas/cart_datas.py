

class CartData(object):
    """配置购物车测试商品数据"""

    # 非农机服务商品pid：30，31,32,38 ->noservice_product
    # 农机服务商品pid：33,34,35,36,37 ->service_product
    # 商品单价均为一千元。

    # pid,total_price,compete_attribute,inquiry_attribute,order_attribute
    test_cart_one_noservice_product_datas = [
        (
            30,
            1000,
            False,
            True,
            True
        ),
        (
            30,
            50000,
            True,
            False,
            False
        )
    ]
