import streamlit as st
from main.bdd_communication import ConnectBbd

def delBot(x):
    # cnx = mysql.connector.connect(host='localhost', user='root', password='password', port='3306', database='crypto',
    #                               auth_plugin='mysql_native_password')
    con = ConnectBbd('localhost', '3306', 'root', 'password', 'crypto', 'mysql_native_password')
    con.delete_bot(x)

con = ConnectBbd( 'localhost', '3306', 'root', 'password','crypto', 'mysql_native_password')

bots = con.get_bots()
bot = [i[1] for i in bots]

if 'my_list' not in st.session_state:
    st.session_state.my_list = bot

for index, item in enumerate(st.session_state.my_list):
    emp = st.empty()
    col1, col2, col3 = emp.columns([9, 1, 1])
    if col2.button("Del", key=f"but{index}"):
        delBot(bots[index][0])
        del st.session_state.my_list[index]
    if col3.button("Edit", key=f"ed{index}"):
        # not implemented - just for example
        pass
    if len(st.session_state.my_list) > index:
        col1.markdown(f'My row item **{item}**. Item index {index}', unsafe_allow_html=True)
    else:
        emp.empty()