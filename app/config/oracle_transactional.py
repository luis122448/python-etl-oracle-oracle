import os
import oracledb
from dotenv import load_dotenv
from utils.path import BASEDIR

# Cargar la variable de entorno
load_dotenv()

DB_ORACLE_USER = os.getenv("DB_ORACLE_USER_TRANSACCIONAL")
DB_ORACLE_PASSWORD = os.getenv("DB_ORACLE_PASSWORD_TRANSACCIONAL")
DB_ORACLE_DSN_TRANSACCIONAL = os.getenv("DB_ORACLE_DSN_TRANSACCIONAL")

print('Instant Client')
oracledb.init_oracle_client()

print('Oracle Transaccional')
def get_oracle_transactional_connection():
    oracle_transactional_connection = oracledb.connect(
        user=DB_ORACLE_USER,
        password=DB_ORACLE_PASSWORD,
        dsn=DB_ORACLE_DSN_TRANSACCIONAL,
        disable_oob=True
    )
    return oracle_transactional_connection

def close_transactional_oracle_connection():
    oracle_transactional_cursor.close()
    oracle_transactional_connection.close()

# Oracle Cursor
oracle_transactional_connection = get_oracle_transactional_connection()
oracle_transactional_cursor = oracle_transactional_connection.cursor()

# Connection test
oracle_transactional_cursor.execute("SELECT * FROM v$version")
version = oracle_transactional_cursor.fetchone()[0]
print("Oracle Server Version:", version)