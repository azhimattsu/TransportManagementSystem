

from tms.domain.models import order
from tms.infrastructure.mysql.mysql_order import MySqlOrder


def test_MySqlOrder_find_data_bycode():
    """find_data_bycode:存在する受注番号"""
    code = order.SlipCode("0000000002")
    rep = MySqlOrder()
    orderinfo: order.OrderInfo = rep.find_data_bycode(code)

    print(orderinfo.order_id.value)


"""コマンド実行"""
test_MySqlOrder_find_data_bycode()
