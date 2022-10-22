

from tms.domain.models import chassis, shared
from tms.infrastructure.mysql.mysql_chassis import MySqlChassis


def test_MySqlChassis_fetch_all_data():
    """fetch_all_data:全件取得"""
    rep = MySqlChassis()
    results = rep.fetch_all_data()

    print(results)


def test_MySqlChassis_find_data_bycode():
    """find_data_bycode:存在する受注番号"""
    code = chassis.ChassisCode("S-084")
    rep = MySqlChassis()
    result: chassis.ChassisInfo = rep.find_data_bycode(code)

    print(result.chassis_id)


def test_MySqlChassis_create_data():
    """create_data:新規登録"""
    entity = chassis.ChassisInfo(chassis.ChassisId("ZZZZ"),
                                  chassis.ChassisCode("ZZZZA"),
                                  chassis.VehicleNumber("横浜あ3318"),
                                  chassis.Size(1),
                                  chassis.Axes(2),
                                  shared.CDateTime("2024-12-31 00:00:00"),
                                  chassis.Model("ABCDEFG"),
                                  shared.UpdateInfo(shared.MailAddress("test010@test.com"),
                                                    shared.MailAddress("test010@test.com"),
                                                    shared.CDateTime("2022-10-01 00:00:00"),
                                                    shared.CDateTime("2022-10-01 00:00:00")))

    rep = MySqlChassis()
    rep.create_data(entity)


"""コマンド実行"""
test_MySqlChassis_fetch_all_data()
test_MySqlChassis_find_data_bycode()
test_MySqlChassis_create_data()
