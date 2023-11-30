# Creando el ambiente virual
python3 -m venv venv

# Ejecutar el ambiente virtual
source venv/bin/activate

# Instalando dependencias del proyecto
pip install -r requirements.txt

# Instalando libaio para el cliente oracle
apt-get install -y libaio1

# Crenado directorio para certificados SSL
mkdir -p app/certs

# Configuracion del SSL
export COUNTRY=PE
export STATE=LIMA
export CITY=LIMA
export ORGANIZATION=''
export ORGANIZATIONAL_UNIT=''
export COMMON_NAME=''
export EMAIL=''

# Generando certificados SSL
openssl req -new -x509 -keyout ./app/certs/key.pem -out ./app/certs/cert.pem -days 365 -nodes -subj "/C=$COUNTRY/ST=$STATE/L=$CITY/O=$ORGANIZATION/OU=$ORGANIZATIONAL_UNIT/CN=$COMMON_NAME/emailAddress=$EMAIL"

# Creando directorio para la wallet
mkdir -p app/wallet