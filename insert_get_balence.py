import mysql.connector
import  pandas as pd
import os

class ConnectBbd:
    def __init__(self, host, port, user, password, database, auth_plugin):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.auth_plugin =auth_plugin
        self.cnx = mysql.connector.connect(host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    port=self.port,
                                    database=self.database,
                                    auth_plugin=self.auth_plugin)

    def insert(self, data):
      cursor =self.cnx.cursor()
      query =  "INSERT INTO  get_balence (dates, crypto_name, crypto_wallet, id_bot ) VALUES  ( %s, %s, %s,%s)"
      cursor.execute(query, data)
      self.cnx.commit()
      cursor.close()
      self.cnx.close()
      return print("value added to database ",data)

    def fetch_all(self):
        cursor =self.cnx.cursor()
        rows = cursor.fetchall()
        return rows

    def frach_all_2(self):
        cursor =self.cnx.cursor()
        cursor.execute("SELECT * FROM get_balence")
        head_rows = cursor.fetchmany(size=2)
        remaining_rows = cursor.fetchall()
        return remaining_rows

def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

if checkFileExistance("/var/www/html/data_db.csv"):
    print("fichier existe")
    os.remove("/var/www/html/data_db.csv")
bot_name="helmi_bot"
user_name="helmi"
sql_password ="Magali_1984"
con = ConnectBbd('localhost','3306','root',sql_password,'cryptos','mysql_native_password')
#all_data = con.fetch_all()
all_data2 = con.frach_all_2()

df_data = pd.DataFrame(all_data2)
df_data.to_csv("/var/www/html/data_db.csv")

print("apparament OK")
