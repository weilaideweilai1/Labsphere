import psycopg2
import getpass

password = getpass.getpass("请输入数据库密码:")

conn = psycopg2.connect(
    dbname = "labsphere_dev",
    user = "gaussdb",
    password = password,
    host = "127.0.0.1",
    port = 15432    
)

cursor = conn.cursor()


cursor.execute("SELECT current_database()")
result1 = cursor.fetchone()
print("库名",result1)

cursor.execute("SELECT current_user")
result2 = cursor.fetchone()
print("用户名:",result2)

cursor.execute("SELECT version()")
result3 = cursor.fetchone()
print("版本号:",result3)

cursor.close()
conn.close()
