import uvicorn, subprocess
import os

# BaseDir
BASEDIR = os.path.dirname(os.path.realpath(__file__))

path_ssl_keyfile = os.path.join(BASEDIR, "certs/key.pem")
path_ssl_certfile = os.path.join(BASEDIR, "certs/cert.pem")

if __name__ == '__main__':
    print("Iniciando Servidor")
    print("DIRECTORY : ", BASEDIR)
    print("ORACLE_HOME : ", os.getenv("ORACLE_HOME"))
    print("LD_LIBRARY_PATH : ", os.getenv("LD_LIBRARY_PATH"))
    print("TNS_ADMIN : ", os.getenv("TNS_ADMIN"))
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8000,
                reload=True,
                ssl_keyfile=path_ssl_keyfile,
                ssl_certfile=path_ssl_certfile,
                )