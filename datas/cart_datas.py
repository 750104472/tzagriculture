

class CartData(object):
    """配置购物车测试商品数据"""

    # 非农机服务商品pid：30，31,32,38 -> noservice_product
    # 农机服务商品pid：33,34,35,36,37 -> service_product
    # 商品单价均为一千元。

    # pid,total_price,compete_attribute,inquiry_attribute,order_attribute
    test_cart_one_noservice_product_datas = [

        (30,49000,False,True,True),
        (30,50000,True,False,False),
        (30,200000, False, False, False),
        (30, 190000, True, False, False)

    ]

    # pid1, total_price1, pid2, total_price2, pid3, total_price3, compete_attribute, inquiry_attribute, order_attribute
    test_cart_three_noservice_product_datas = [
        (30,20000,31,20000,32,9000,False,False,True),
        (30, 20000, 31, 20000, 32, 10000, False, False, True),
        (30, 50000, 31, 50000, 32, 50000, False, False, False),
        (30, 100000, 31, 50000, 32, 50000, False, False, False)

    ]
