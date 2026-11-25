import getpass
from sqlalchemy import create_engine,text
from sqlalchemy.engine import URL

password  = getpass.getpass("请输入数据库密码:")

url = URL.create(
    drivername= "opengauss+psycopg2",
    username= "gaussdb",
    password=password,
    host = "127.0.0.1",
    port = 15432,
    database = "labsphere_dev"
)

engine = create_engine(url)

with engine.connect() as conn:
    result1 = conn.execute(text("SELECT current_database();"))
    print("当前数据库:",result1.scalar())

    result2 = conn.execute(text("SELECT current_user;"))
    print("当前用户:",result2.scalar())

    result3 = conn.execute(text("SELECT version();"))
    print("当前版本:",result3.scalar()) 