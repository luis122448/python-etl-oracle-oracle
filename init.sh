# 
cp -p ./app/wallet/sqlnet.ora ./oracle_home/instantclient_21_12/network/admin
cp -p ./app/wallet/tnsnames.ora ./oracle_home/instantclient_21_12/network/admin
cp -p ./app/wallet/cwallet.sso ./oracle_home/instantclient_21_12/network/admin

# Inicializando Variables de Entorno
export DPI_DEBUG_LEVEL=64
export TNS_ADMIN="$PWD/app/wallet"
export LD_LIBRARY_PATH="$PWD/oracle_home/instantclient_21_12"

# Activando ambiente virtual
source venv/bin/activate

# Iniciando Aplicacion
python app/server.py