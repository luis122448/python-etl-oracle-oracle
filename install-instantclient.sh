unzip ./oracle_home/instantclient-basic-linux.x64-21.12.0.0.0dbru.zip -d /opt/oracle_home
mv ./oracle_home/instantclient_21_12 /opt/oracle_home/instantclient
cp ./app/wallet/sqlnet.ora /opt/oracle_home/instantclient/network/admin
cp ./app/wallet/tnsnames.ora /opt/oracle_home/instantclient/network/admin
cp ./app/wallet/cwallet.sso /opt/oracle_home/instantclient/network/admin

export DPI_DEBUG_LEVEL=64