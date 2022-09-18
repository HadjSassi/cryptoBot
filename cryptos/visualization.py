import mysql.connector
import pandas as pd
import plotly.express as px
import streamlit as st

#Connect with database
#Please verify the informations below to avoid exceptions
cnx = mysql.connector.connect(host='localhost',user='root',password='system',port='3306',database='cryptos',auth_plugin='mysql_native_password')
'''
We're going to show 2 plots the first crypto wallet by date for each crypto_name
and the other crypto wallet by date for each bot_name
the instructions will be merged together just the first we're going to seperate between them
'''
#fetch data for crypto wallet by date for each crypto name
cursor = cnx.cursor()
query = "select dates,crypto_name,crypto_wallet from get_balence;"
cursor.execute(query)
myresult = cursor.fetchall()

#fetch data for crypto wallet by date for each bot name
query = "select dates, crypto_wallet,nom_bot from get_balence, bots where (get_balence.id_bot = bots.bot_id);"
cursor.execute(query)
myresult2= cursor.fetchall()


#create a dataframe from the table get_balence
#1
column_names = ['dates','crypto_name','crypto_wallet']
workbook = pd.DataFrame(columns=column_names)
for i in myresult:
    workbook.loc[len(workbook.index)] = i
#2
column_names2 = ['dates','crypto_wallet','nom_bot']
workbook2 = pd.DataFrame(columns=column_names2)
for i in myresult2:
    workbook2.loc[len(workbook2.index)] = i

#correct fields to the true type property
#1
workbook["dates"] = pd.to_datetime(workbook['dates'])
workbook["crypto_wallet"] = pd.to_numeric(workbook['crypto_wallet'])
#2
workbook2["dates"] = pd.to_datetime(workbook2['dates'])
workbook2["crypto_wallet"] = pd.to_numeric(workbook2['crypto_wallet'])

#normalize crypto_name field to delete the redundent "/USDT"
#1
for i in range(workbook.shape[0]):
    workbook.iloc[i,1] = workbook.iloc[i,1].replace('/USDT','')

#Create a dictionnary that differs between names
#1
list_df = {}
for i in workbook['crypto_name'].unique() :
    l = ['dates',i]
    d = pd.DataFrame(columns=l)
    list_df[i] = d
#2
list_df2 = {}
for i in workbook2['nom_bot'].unique() :
    l = ['dates',i]
    d = pd.DataFrame(columns=l)
    list_df2[i] = d

#Fill the dictionnary with the appropriate values
#1
for i in workbook.values:
    for j,k in list_df.items():
        if (i[1] == j):
            k.loc[len(k.index)] = [i[0],i[2]]
#2
for i in workbook2.values:
    for j,k in list_df2.items():
        if (i[2] == j):
            k.loc[len(k.index)] = [i[0],i[1]]


#Make the final dataframe that contains all the necessary values
#1
dff = pd.concat(list(list_df.values()))
dff = dff.sort_values('dates',ignore_index=True)
#2
dff2 = pd.concat(list(list_df2.values()))
dff2 = dff2.sort_values('dates',ignore_index=True)

#fill the nan values with a logic one
#1
dff = dff.fillna(method='ffill')
dff = dff.fillna(0)
#2
dff2 = dff2.fillna(method='ffill')
dff2 = dff2.fillna(0)

#create a plotly chart
fig1 = px.line(dff, x="dates", y=dff.columns, title='cryptos showed by date and wallet')
fig2 = px.line(dff2, x="dates", y=dff2.columns, title='bots showed by date and wallet')
#show the chart with streamlit
st.plotly_chart(fig2)
st.plotly_chart(fig1)
