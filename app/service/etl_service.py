import oracledb
import time
import os
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
from querys.oracle_query import query_dataset_example
from schemas.api_response_schema import ApiResponseSchema
from config.oracle_transactional import oracle_transactional_cursor, oracle_transactional_connection
from config.oracle_datawarehouse import oracle_datawarehouse_cursor, oracle_datawarehouse_connection
from utils.path import PATHLOG

def etl_dataset_example(id_cia: str) -> ApiResponseSchema:
    try:

        # Inicializar resultado con un valor predeterminado
        object = ApiResponseSchema(
            status=1, message="OK", id_cia=id_cia, timestamp="")
        intermediate_time = 0

        # Consulta de selección de datos en Oracle
        oracle_query = query_dataset_example(id_cia)
        start_time = time.time()  # Tiempo de inicio

        # Construir la sentencia DELETE
        delete_query = f'''
            DELETE FROM DW_DATASET_EXAMPLE
            WHERE ID_CIA = {id_cia}
        '''

        # Ejecutar la sentencia DELETE
        oracle_datawarehouse_cursor.execute(delete_query)
        # Confirmar los cambios
        oracle_datawarehouse_connection.commit()
        # Ejecución de la consulta en Oracle
        oracle_transactional_cursor.execute(oracle_query)
        # Recorrido de los resultados y escritura en MySQL en bloques
        rows = oracle_transactional_cursor.fetchall()
        batch_size = 1000  # Tamaño del bloque de inserción
        records = len(rows)  # Numero de Registros

        # Tiempo Intermedio
        intermediate_time = time.time()

        if rows is None or records == 0:
            object.status = 0
            object.message = "No se encontran registros, para procesar el ETL verifique el rango de fechas"
        else:
            for i in range(0, records, batch_size):
                batch_rows = rows[i:i + batch_size]
                placeholders = ','.join([':' + str(index + 1) for index in range(len(batch_rows[0]))])
                insert_query = f'INSERT INTO DW_DATASET_EXAMPLE VALUES ({placeholders})'
                oracle_datawarehouse_cursor.executemany(insert_query, batch_rows)
                oracle_datawarehouse_connection.commit()
            object.status = 1
            object.message = "Proceso finalizado, se actualizaron un total de " + \
                str(records) + " registros!"
        
    except oracledb.Error as e:
        object.status = 1.2
        object.message = f"ERROR (ORACLE) : {e}"
    except Exception as e:
        object.status = 1.2
        object.message = f"ERROR : {e}"
    finally:
        end_time = time.time()  # Tiempo de finalización
        # Tiempo transcurrido en segundos
        elapsed_time = round(end_time - start_time, 2)
        select_time = round(intermediate_time - start_time, 2)
        insert_time = round(end_time - intermediate_time, 2)
        object.timestamp = (
            "Tiempo Total : "
            + str(elapsed_time)
            + " segundos!"
            + "\n Tiempo Select : "
            + str(select_time)
            + " segundos!"
            + "\n Tiempo Insert : "
            + str(insert_time)
            + " segundos!"
        )
        return object
