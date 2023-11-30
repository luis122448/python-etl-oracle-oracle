# Inicializando Variables de Entorno
export DPI_DEBUG_LEVEL=64
export TNS_ADMIN=~/python-etl-oracle/app/wallet
export LD_LIBRARY_PATH=~/python-etl-oracle/oracle_home/instantclient_21_12

# Activando ambiente virtual
source venv/bin/activate

# Iniciando Aplicacion
python app/server.py