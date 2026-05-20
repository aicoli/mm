import pymysql

def get_db_conn():
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="",   # 请修改为实际密码
            database="school",
            charset="utf8mb4"
        )
        return conn
    except pymysql.Error as e:
        print(f"数据库连接失败: {e}")
        return None

def get_all_class():
    conn = get_db_conn()
    if conn is None:
        print("无法获取数据库连接，返回空列表")
        return []
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT cid, cname FROM class")
            return cur.fetchall()
    except pymysql.Error as e:
        print(f"查询失败: {e}")
        return []
    finally:
        conn.close()