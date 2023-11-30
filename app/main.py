from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.etl_router import etl_router
from utils.path import create_dir_logs, get_path_log, get_path_project
from config.oracle_transactional import oracle_transactional_cursor, oracle_transactional_connection
from config.oracle_datawarehouse import oracle_datawarehouse_cursor, oracle_datawarehouse_connection
from scheduler.etl_scheduler import initEtlScheduler, stopEtlScheduler

app = FastAPI()
app.title = "App ETL Oracle - Oracle"
app.version = "1.0.0"
app.description = "ETL"
app.docs_url = "/docs"
app.include_router(etl_router)

# Configura CORS para permitir todas las solicitudes desde cualquier origen (ajusta según tus necesidades)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    print("Startup")
    print('Path Project: ', get_path_project())
    print('Path Log: ', get_path_log())
    initEtlScheduler()
    create_dir_logs()

@app.on_event("shutdown")
async def shutdown():
    stopEtlScheduler()
    print("Shutdown")