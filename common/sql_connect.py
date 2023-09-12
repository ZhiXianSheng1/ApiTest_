import pymysql


def connect_mysql():
    try:
        con = pymysql.connect(
            host="",
            user="Gongwei",
            password="123456",
            database="nba_test",
            charset='utf8'
        )
    except pymysql.Error as e:
        print("SQL连接失败:", e)
    c = con.cursor()
    c.execute('USE NBA_TEST;')
    # result = c.fetchall()
    # for row in result:
    #     print(row)
    con.commit()
    con.close()
