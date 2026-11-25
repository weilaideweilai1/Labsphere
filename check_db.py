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

cursor.execute("SELECT 1")

result = cursor.fetchone()
print(result)

cursor.close()
conn.close()