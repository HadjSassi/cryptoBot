import mysql.connector
import pandas as pd
import plotly.express as px
import streamlit as st

#Connect with database
#Please verify the informations below to avoid exceptions
cnx = mysql.connector.connect(host='localhost',user='root',password='system',port='3306',database='cryptos',auth_plugin='mysql_native_password')

#fetch all balences in the table get_balence
cursor = cnx.cursor()
query = "select * from get_balence;"
cursor.execute(query)
myresult = cursor.fetchall()

#create a dataframe from the table get_balence
column_names = ['id_get_balence','dates','crypto_name','crypto_wallet','id_bot']
workbook = pd.DataFrame(columns=column_names)
for i in myresult:
    workbook.loc[len(workbook.index)] = i

#correct fields to the true type property
workbook["dates"] = pd.to_datetime(workbook['dates'])
workbook["crypto_wallet"] = pd.to_numeric(workbook['crypto_wallet'])

#delete useless columns
workbook = workbook.drop(["id_get_balence","id_bot"], axis=1)

#normalize crypto_name field to delete the redundent "/USDT"
for i in range(workbook.shape[0]):
    workbook.iloc[i,1] = workbook.iloc[i,1].replace('/USDT','')

#Create a dictionnary that differs between crypto_names
list_df = {}
for i in workbook['crypto_name'].unique() :
    l = ['dates',i]
    d = pd.DataFrame(columns=l)
    list_df[i] = d

#Fill the dictionnary with the appropriate values
for i in workbook.values:
    for j,k in list_df.items():
        if (i[1] == j):
            k.loc[len(k.index)] = [i[0],i[2]]

#Make the final dataframe that contains all the necessary values
dff = pd.concat(list(list_df.values()))
dff = dff.sort_values('dates',ignore_index=True)

#fill the nan values with a logic one
dff = dff.fillna(method='ffill')
dff = dff.fillna(0)

#create a plotly chart
fig2 = px.line(dff, x="dates", y=dff.columns, title='cryptos showed by date and wallet')

#show the chart with streamlit
st.plotly_chart(fig2)
