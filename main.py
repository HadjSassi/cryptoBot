import streamlit as st
import pandas as pd
import plotly.express as px

#read from database
workbook = pd.read_excel('a.xlsx')

#Convert time column to a date column
workbook["time"] = pd.to_datetime(workbook['time'])

#prepare the columns
time = workbook['time']
value = workbook['coeff mult.5']
value1 = workbook['coeff mult']
value2 = workbook['coeff mult.1']
value3 = workbook['coeff mult.2']
value4 = workbook['coeff mult.3']
value5 = workbook['coeff mult.4']

#create the first dataframe
df1 = pd.concat([time,value], axis=1)
df1.rename(columns={'coeff mult.5':'Bot Max'},inplace=True)

#prepare the plot of the first dataframe
fig = px.line(df1, x="time", y=df1.columns,
              title='custom tick labels')

#create the second  dataframe
df2 = pd.concat([time,value1,value2,value3,value4,value5],axis=1)
df2.rename(columns={'coeff mult':'ETH','coeff mult.1':'DOT','coeff mult.2':'DODGE','coeff mult.3':'ADA','coeff mult.4':'BNB'},inplace=True)

#prepare the plot of the second dataframe
fig2 = px.line(df2, x="time", y=df2.columns,
              title='custom tick labels')

#showing the two plots
st.plotly_chart(fig)
st.plotly_chart(fig2)
