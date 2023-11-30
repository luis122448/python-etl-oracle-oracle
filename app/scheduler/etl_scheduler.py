from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, time

# Importa tus funciones de ETL
from service.etl_service import etl_dataset_example

# Crea una instancia del planificador
etl_scheduler = BackgroundScheduler()

# Define tus funciones de ETL que se ejecutarán
def ejecutar_etl_diary(id_cia: str):
    # etl_dataset_example(id_cia)
    print("Ejecutando ETL cada dia")

def ejecutar_etl_hour(id_cia: str):
    # etl_dataset_example(id_cia)
    print("Ejecutando ETL cada hora")

def ejecutar_etl_minute(id_cia: str):
    # etl_dataset_example(id_cia)
    print("Ejecutando ETL cada minuto")

# Agrega la tarea al planificador para ejecutarse todos los días a la 1:00 a.m.
etl_scheduler.add_job(
    ejecutar_etl_diary,
    trigger='cron',
    hour=1,
    minute=0,
    second=0,
    args=['66'],
)

etl_scheduler.add_job(
    ejecutar_etl_hour,
    trigger='cron',
    hour='*',
    minute=0,
    second=0,
    args=['66'],
)

etl_scheduler.add_job(
    ejecutar_etl_minute,
    trigger='cron',
    hour='*',
    minute='*',
    second=0,
    args=['66'],
)

# Inicia el planificador
def initEtlScheduler():
    print("Iniciando planificador")
    etl_scheduler.start()

# Detiene el planificador
def stopEtlScheduler():
    print("Deteniendo planificador")
    etl_scheduler.shutdown()