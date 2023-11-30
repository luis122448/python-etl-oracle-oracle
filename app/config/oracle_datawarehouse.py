import os
import oracledb
from dotenv import load_dotenv
from utils.path import BASEDIR

# Cargar la variable de entorno
load_dotenv()

DB_ORACLE_USER = os.getenv("DB_ORACLE_USER_DATAWAREHOUSE")
DB_ORACLE_PASSWORD = os.getenv("DB_ORACLE_PASSWORD_DATAWAREHOUSE")
DB_ORACLE_DSN_DATAWAREHOUSE = os.getenv("DB_ORACLE_DSN_DATAWAREHOUSE")

print('Oracle Datawarehouse')

def get_oracle_datawarehouse_connection():
    oracle_datawarehouse_connection = oracledb.connect(
        user=DB_ORACLE_USER,
        password=DB_ORACLE_PASSWORD,
        dsn=DB_ORACLE_DSN_DATAWAREHOUSE
    )
    return oracle_datawarehouse_connection

def close_oracle_datawarehouse_connection():
    oracle_datawarehouse_cursor.close()
    oracle_datawarehouse_connection.close()

# Oracle Cursor
oracle_datawarehouse_connection = get_oracle_datawarehouse_connection()
oracle_datawarehouse_cursor = oracle_datawarehouse_connection.cursor()

# Connection test
oracle_datawarehouse_cursor.execute("SELECT * FROM v$version")
version = oracle_datawarehouse_cursor.fetchone()[0]
print("Oracle Server Version:", version)