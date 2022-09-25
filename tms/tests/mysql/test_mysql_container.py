from tms.mysqlinfrastructure.mysql_container import MySqlContainers


def Test_MySqlContainers_fetch_all_data():
    rep = MySqlContainers()
    values = rep.fetch_all_data()
    length = len(values)
    print(length)
    print(values)


Test_MySqlContainers_fetch_all_data()
