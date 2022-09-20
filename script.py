import mysql.connector
import pandas as pd
import ftx
from  Test.bdd_communication import ConnectBbd
from datetime import datetime

# First Task
# Get All the necessary columns from the database

cnx = mysql.connector.connect(host='localhost', user='root', password='system', port='3306', database='cryptos',
                              auth_plugin='mysql_native_password')
cursor = cnx.cursor()
query = "select * from params_bot_trix;"
cursor.execute(query)
myresult = cursor.fetchall()

# Trix Set : id, api_key, secret_key, sub_account, pair_symbol, trix_length, trix_signal, stoch_top, stoch_bottom,
# stoch_RSI, bot_id

# Second Task
# For each line launch the api and get the crypto_wallet value

for i in myresult:
    client = ftx.FtxClient(
        api_key=i[1],
        api_secret=i[2],
        subaccount_name=i[3]
    )
    listBalances = sorted(client.get_balances(),key= lambda d : d['total'], reverse= True)
    con = ConnectBbd('localhost', '3306', 'root', 'system', 'cryptos', 'mysql_native_password')
    con.insert_trix_balence(datetime.now(), f"Trix : {i[4]}_len{i[5]}_sign{i[6]}_top{i[7]}_bottom{i[8]}_RSI{i[9]}", listBalances[0]['total'], i[10])


