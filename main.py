import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

workbook = pd.read_excel('a.xlsx')
workbook["time"] = pd.to_datetime(workbook['time'])
time = workbook['time']
value = workbook['coeff mult.5']

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(time, value);
font1 = {'family':'serif','color':'green','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
ax.set_title("First figure : Visualisation BotMax1", fontdict = font1)
ax.set_xlabel("Date", fontdict = font2)
ax.set_ylabel("Coeff mult", fontdict = font2)



value1 = workbook['coeff mult']
value2 = workbook['coeff mult.1']
value3 = workbook['coeff mult.2']
value4 = workbook['coeff mult.3']
value5 = workbook['coeff mult.4']
value6 = workbook['coeff mult.5']

fig1, fig0 = plt.subplots(figsize=(10, 5))

fig0.plot(time, value1,label='eth')
fig0.plot(time, value2,label='dot')
fig0.plot(time, value3,label='dodge')
fig0.plot(time, value4,label='ada')
fig0.plot(time, value5,label='bnb')
font1 = {'family':'serif','color':'red','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
fig0.set_title("First figure : Visualisation", fontdict = font1)
fig0.set_xlabel("Date", fontdict = font2)
fig0.set_ylabel("Coeff mult", fontdict = font2)
fig0.legend()


st.pyplot(fig1)
st.pyplot(fig)