import json
import os
import streamlit as st
import pandas as pd

import pymysql
import requests
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import PIL
from PIL import Image
import matplotlib.pyplot as plt
import git
#aggretransaction
path1="C:/Users/Dheeraj/Desktop/phonepay/pulse/data/aggregated/transaction/country/india/state/"
aggregate_transaction_list=os.listdir(path1)
COLUMNS1={"States":[], "Years":[], "Quaters":[], "Transactiontype":[],"Transactioncount":[],"Transactionamount":[]}
for states in aggregate_transaction_list:
    currentstate=path1+states+"/"
    aggre_year_list=os.listdir(currentstate)
    for year in aggre_year_list:
        curr_year=currentstate+year+"/"
        aggre_file_list=os.listdir(curr_year)
        for file in aggre_file_list:
            curr_file=curr_year+file
            datas=open(curr_file,"r")
            A1=json.load(datas)
            for i in A1["data"]["transactionData"]:
                name=i["name"]
                count=i["paymentInstruments"][0]["count"]
                amount=i["paymentInstruments"][0]["amount"]
                COLUMNS1["Transactiontype"].append(name)
                COLUMNS1["Transactioncount"].append(count)
                COLUMNS1["Transactionamount"].append(amount)
                COLUMNS1["States"].append(states)
                COLUMNS1["Years"].append(year)
                COLUMNS1["Quaters"].append(int(file.strip(".json")))
aggretransaction=pd.DataFrame(COLUMNS1)
aggretransaction["States"] = aggretransaction["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
aggretransaction["States"] = aggretransaction["States"].str.replace("-"," ")
aggretransaction["States"] = aggretransaction["States"].str.title()
aggretransaction['States'] = aggretransaction['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

custom_state_list = ['Andaman & Nicobar',
 'Andhra Pradesh',
 'Arunachal Pradesh',
 'Assam',
 'Bihar',
 'Chandigarh',
 'Chhattisgarh',
 'Dadra and Nagar Haveli and Daman and Diu',
 'Delhi',
 'Goa',
 'Gujarat',
 'Haryana',
 'Himachal Pradesh',
 'Jammu & Kashmir',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Ladakh',
 'Lakshadweep',
 'Madhya Pradesh',
 'Maharashtra',
 'Manipur',
 'Meghalaya',
 'Mizoram',
 'Nagaland',
 'Odisha',
 'Puducherry',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telangana',
 'Tripura',
 'Uttar Pradesh',
 'Uttarakhand',
 'West Bengal']
aggretransaction['States'] = aggretransaction['States'].replace(dict(zip(aggregate_transaction_list, custom_state_list)))

#aggreuser
path2="C:/Users/Dheeraj/Desktop/phonepay/pulse/data/aggregated/user/country/india/state/"
aggregate_user_list=os.listdir(path2)
COLUMNS2={"States":[], "Years":[], "Quaters":[], "Brands":[],"Transactioncount":[],"Percentage":[]}
for states in aggregate_user_list:
    currentstate=path2+states+"/"
    aggre_year_list=os.listdir(currentstate)
    for year in aggre_year_list:
        curr_year=currentstate+year+"/"
        aggre_file_list=os.listdir(curr_year)
        for file in aggre_file_list:
            curr_file=curr_year+file
            datas=open(curr_file,"r")
            B1=json.load(datas)
            try:
                for i in B1["data"]["usersByDevice"]:
                    brand=i["brand"]
                    count=i["count"]
                    percentage=i["percentage"]
                    COLUMNS2["Brands"].append(brand)
                    COLUMNS2["Transactioncount"].append(count)
                    COLUMNS2["Percentage"].append(percentage)
                    COLUMNS2["States"].append(states)
                    COLUMNS2["Years"].append(year)
                    COLUMNS2["Quaters"].append(int(file.strip(".json")))
            except:
                pass        

aggreuser=pd.DataFrame(COLUMNS2)
aggreuser["States"] = aggreuser["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
aggreuser["States"] = aggreuser["States"].str.replace("-"," ")
aggreuser["States"] = aggreuser["States"].str.title()
aggreuser['States'] = aggreuser['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
custom_state_list = ['Andaman & Nicobar',
 'Andhra Pradesh',
 'Arunachal Pradesh',
 'Assam',
 'Bihar',
 'Chandigarh',
 'Chhattisgarh',
 'Dadra and Nagar Haveli and Daman and Diu',
 'Delhi',
 'Goa',
 'Gujarat',
 'Haryana',
 'Himachal Pradesh',
 'Jammu & Kashmir',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Ladakh',
 'Lakshadweep',
 'Madhya Pradesh',
 'Maharashtra',
 'Manipur',
 'Meghalaya',
 'Mizoram',
 'Nagaland',
 'Odisha',
 'Puducherry',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telangana',
 'Tripura',
 'Uttar Pradesh',
 'Uttarakhand',
 'West Bengal']

aggreuser['States'] = aggreuser['States'].replace(dict(zip(aggregate_user_list, custom_state_list)))
 
#maptransactionhistory
path3="C:/Users/Dheeraj/Desktop/phonepay/pulse/data/map/transaction/hover/country/india/state/"
map_transaction_list=os.listdir(path3)
COLUMNS3={"States":[], "Years":[], "Quaters":[], "Districts":[],"Transactioncount":[],"Transactionamount":[]}
for states in map_transaction_list:
    currentstate=path3+states+"/"
    aggre_year_list=os.listdir(currentstate)
    for year in aggre_year_list:
        curr_year=currentstate+year+"/"
        aggre_file_list=os.listdir(curr_year)
        for file in aggre_file_list:
            curr_file=curr_year+file
            datas=open(curr_file,"r")
            C1=json.load(datas)
            for i in C1["data"]["hoverDataList"]:
                name=i["name"]
                count=i["metric"][0]["count"]
                amount=i["metric"][0]["amount"]
                COLUMNS3["Districts"].append(name)
                COLUMNS3["Transactioncount"].append(count)
                COLUMNS3["Transactionamount"].append(amount)
                COLUMNS3["States"].append(states)
                COLUMNS3["Years"].append(year)
                COLUMNS3["Quaters"].append(int(file.strip(".json")))
maptranshist=pd.DataFrame(COLUMNS3)
maptranshist["States"] = maptranshist["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
maptranshist["States"] = maptranshist["States"].str.replace("-"," ")
maptranshist["States"] = maptranshist["States"].str.title()
maptranshist['States'] = maptranshist['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
custom_state_list = ['Andaman & Nicobar',
 'Andhra Pradesh',
 'Arunachal Pradesh',
 'Assam',
 'Bihar',
 'Chandigarh',
 'Chhattisgarh',
 'Dadra and Nagar Haveli and Daman and Diu',
 'Delhi',
 'Goa',
 'Gujarat',
 'Haryana',
 'Himachal Pradesh',
 'Jammu & Kashmir',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Ladakh',
 'Lakshadweep',
 'Madhya Pradesh',
 'Maharashtra',
 'Manipur',
 'Meghalaya',
 'Mizoram',
 'Nagaland',
 'Odisha',
 'Puducherry',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telangana',
 'Tripura',
 'Uttar Pradesh',
 'Uttarakhand',
 'West Bengal']

maptranshist['States'] = maptranshist['States'].replace(dict(zip(map_transaction_list, custom_state_list)))
#mapuser
path4="C:/Users/Dheeraj/Desktop/phonepay/pulse/data/map/user/hover/country/india/state/"
map_user_list=os.listdir(path4)
COLUMNS4={"States":[], "Years":[], "Quaters":[], "Districts":[],"Registereduser":[],"Appsopen":[]}
for states in map_user_list:
    currentstate=path4+states+"/"
    aggre_year_list=os.listdir(currentstate)
    for year in aggre_year_list:
        curr_year=currentstate+year+"/"
        aggre_file_list=os.listdir(curr_year)
        for file in aggre_file_list:
            curr_file=curr_year+file
            datas=open(curr_file,"r")
            D1=json.load(datas)
            for i in D1["data"]["hoverData"].items():
                district=i[0]
                registereduser = i[1]["registeredUsers"]
                appopens = i[1]["appOpens"]
                COLUMNS4["Districts"].append(district)
                COLUMNS4["Registereduser"].append(registereduser)
                COLUMNS4["Appsopen"].append(appopens)
                COLUMNS4["States"].append(states)
                COLUMNS4["Years"].append(year)
                COLUMNS4["Quaters"].append(int(file.strip(".json")))
mapuserlist=pd.DataFrame(COLUMNS4)
mapuserlist["States"] = mapuserlist["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
mapuserlist["States"] = mapuserlist["States"].str.replace("-"," ")
mapuserlist["States"] = mapuserlist["States"].str.title()
mapuserlist['States'] = mapuserlist['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
custom_state_list = ['Andaman & Nicobar',
 'Andhra Pradesh',
 'Arunachal Pradesh',
 'Assam',
 'Bihar',
 'Chandigarh',
 'Chhattisgarh',
 'Dadra and Nagar Haveli and Daman and Diu',
 'Delhi',
 'Goa',
 'Gujarat',
 'Haryana',
 'Himachal Pradesh',
 'Jammu & Kashmir',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Ladakh',
 'Lakshadweep',
 'Madhya Pradesh',
 'Maharashtra',
 'Manipur',
 'Meghalaya',
 'Mizoram',
 'Nagaland',
 'Odisha',
 'Puducherry',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telangana',
 'Tripura',
 'Uttar Pradesh',
 'Uttarakhand',
 'West Bengal']

mapuserlist['States'] = mapuserlist['States'].replace(dict(zip(map_user_list, custom_state_list)))

#toptransaction
path5="C:/Users/Dheeraj/Desktop/phonepay/pulse/data/top/transaction/country/india/state/"
top_transaction_list=os.listdir(path5)
COLUMNS5={"States":[], "Years":[], "Quaters":[], "Pincodes":[],"Transactioncount":[],"Transactionamount":[]}
for states in top_transaction_list:
    currentstate=path5+states+"/"
    aggre_year_list=os.listdir(currentstate)
    for year in aggre_year_list:
        curr_year=currentstate+year+"/"
        aggre_file_list=os.listdir(curr_year)
        for file in aggre_file_list:
            curr_file=curr_year+file
            datas=open(curr_file,"r")
            E1=json.load(datas)
            for i in E1["data"]["pincodes"]:
                entityName = i["entityName"]
                count = i["metric"]["count"]
                amount = i["metric"]["amount"]
                COLUMNS5["Pincodes"].append(entityName)
                COLUMNS5["Transactioncount"].append(count)
                COLUMNS5["Transactionamount"].append(amount)
                COLUMNS5["States"].append(states)
                COLUMNS5["Years"].append(year)
                COLUMNS5["Quaters"].append(int(file.strip(".json")))
toptransactlist=pd.DataFrame(COLUMNS5)
toptransactlist["States"] = toptransactlist["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
toptransactlist["States"] = toptransactlist["States"].str.replace("-"," ")
toptransactlist["States"] = toptransactlist["States"].str.title()
toptransactlist['States'] = toptransactlist['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

custom_state_list = ['Andaman & Nicobar',
 'Andhra Pradesh',
 'Arunachal Pradesh',
 'Assam',
 'Bihar',
 'Chandigarh',
 'Chhattisgarh',
 'Dadra and Nagar Haveli and Daman and Diu',
 'Delhi',
 'Goa',
 'Gujarat',
 'Haryana',
 'Himachal Pradesh',
 'Jammu & Kashmir',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Ladakh',
 'Lakshadweep',
 'Madhya Pradesh',
 'Maharashtra',
 'Manipur',
 'Meghalaya',
 'Mizoram',
 'Nagaland',
 'Odisha',
 'Puducherry',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telangana',
 'Tripura',
 'Uttar Pradesh',
 'Uttarakhand',
 'West Bengal']

toptransactlist['States'] = toptransactlist['States'].replace(dict(zip(top_transaction_list, custom_state_list)))

#topuser
path6="C:/Users/Dheeraj/Desktop/phonepay/pulse/data/top/user/country/india/state/"
top_user_list=os.listdir(path6)
COLUMNS6={"States":[], "Years":[], "Quaters":[], "Pincodes":[],"Registereduser":[]}
for states in top_user_list:
    currentstate=path6+states+"/"
    aggre_year_list=os.listdir(currentstate)
    for year in aggre_year_list:
        curr_year=currentstate+year+"/"
        aggre_file_list=os.listdir(curr_year)
        for file in aggre_file_list:
            curr_file=curr_year+file
            datas=open(curr_file,"r")
            F1=json.load(datas)
            for i in F1["data"]["pincodes"]:
                name = i["name"]
                registeredusers = i["registeredUsers"]
                COLUMNS6["Pincodes"].append(name)
                COLUMNS6["Registereduser"].append(registeredusers)
                COLUMNS6["States"].append(states)
                COLUMNS6["Years"].append(year)
                COLUMNS6["Quaters"].append(int(file.strip(".json")))
topuser=pd.DataFrame(COLUMNS6)
topuser["States"] = topuser["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
topuser["States"] = topuser["States"].str.replace("-"," ")
topuser["States"] = topuser["States"].str.title()
topuser['States'] = topuser['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
custom_state_list = ['Andaman & Nicobar',
 'Andhra Pradesh',
 'Arunachal Pradesh',
 'Assam',
 'Bihar',
 'Chandigarh',
 'Chhattisgarh',
 'Dadra and Nagar Haveli and Daman and Diu',
 'Delhi',
 'Goa',
 'Gujarat',
 'Haryana',
 'Himachal Pradesh',
 'Jammu & Kashmir',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Ladakh',
 'Lakshadweep',
 'Madhya Pradesh',
 'Maharashtra',
 'Manipur',
 'Meghalaya',
 'Mizoram',
 'Nagaland',
 'Odisha',
 'Puducherry',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telangana',
 'Tripura',
 'Uttar Pradesh',
 'Uttarakhand',
 'West Bengal']

topuser['States'] = topuser['States'].replace(dict(zip(top_user_list, custom_state_list)))

#SQL 
mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="Chunnu@123",
  database="phonepay")
mycursor=mydb.cursor()

#aggregated transaction table  
def Agg_trans_tab():
    drop_query = '''drop table if exists aggregated_transaction'''
    mycursor.execute(drop_query)


    mycursor.execute('''CREATE TABLE if not exists aggregated_transaction (States varchar(50),
                                                                        Years int,
                                                                        Quaters int,
                                                                        Transactiontype varchar(50),
                                                                        Transactioncount bigint,
                                                                        Transactionamount bigint
                                                                        )''')

    for index,row in aggretransaction.iterrows():
        insert_query1 = '''INSERT INTO aggregated_transaction (States, Years, Quaters, Transactiontype, Transactioncount, Transactionamount)
                                                            values(%s,%s,%s,%s,%s,%s)'''
        values = (row["States"],
                row["Years"],
                row["Quaters"],
                row["Transactiontype"],
                row["Transactioncount"],
                row["Transactionamount"]
                )
        mycursor.execute(insert_query1,values)
        mydb.commit()
#aggregatted user table
def Agg_user_table():
    drop_query = '''drop table if exists aggregated_user'''
    mycursor.execute(drop_query)


    mycursor.execute('''CREATE TABLE if not exists aggregated_user (States varchar(50),
                                                                Years int,
                                                                Quaters int,
                                                                Brands varchar(50),
                                                                Transactioncount bigint,
                                                                Percentage float)''')

    for index,row in aggreuser.iterrows():
        insert_query2 = '''INSERT INTO aggregated_user (States, Years, Quaters, Brands, Transactioncount, Percentage)
                                                        values(%s,%s,%s,%s,%s,%s)'''
        values = (row["States"],
                row["Years"],
                row["Quaters"],
                row["Brands"],
                row["Transactioncount"],
                row["Percentage"])
        mycursor.execute(insert_query2,values)
        mydb.commit()

#map transaction table
def map_trans_table():
    drop_query = '''drop table if exists map_transaction'''
    mycursor.execute(drop_query)


    mycursor.execute('''CREATE TABLE if not exists map_transaction (States varchar(50),
                                                                Years int,
                                                                Quaters int,
                                                                Districts varchar(80),
                                                                Transactioncount bigint,
                                                                Transactionamount float)''')

    for index,row in maptranshist.iterrows():
                insert_query3 = '''
                    INSERT INTO map_transaction (States, Years, Quaters, Districts, Transactioncount, Transactionamount)
                    VALUES (%s, %s, %s, %s, %s, %s)

                '''
                values = (
                    row["States"],
                    row["Years"],
                    row["Quaters"],
                    row["Districts"],
                    row["Transactioncount"],
                    row["Transactionamount"]
                )
                mycursor.execute(insert_query3,values)
                mydb.commit()

#map user table
def map_user_table():
    drop_query = '''drop table if exists map_user'''
    mycursor.execute(drop_query)


    
    mycursor.execute('''CREATE TABLE if not exists map_user (States varchar(50),
                                                            Years int,
                                                            Quaters int,
                                                            Districts varchar(50),
                                                            Registereduser bigint,
                                                            Appsopen bigint)''')

    for index,row in mapuserlist.iterrows():
        insert_query4 = '''INSERT INTO map_user (States, Years, Quaters, Districts, Registereduser, Appsopen)
                            values(%s,%s,%s,%s,%s,%s)'''
        values = (row["States"],
                row["Years"],
                row["Quaters"],
                row["Districts"],
                row["Registereduser"],
                row["Appsopen"])
        mycursor.execute(insert_query4,values)
        mydb.commit()

#top transaction table
def top_transaction_table():
    drop_query = '''drop table if exists top_transaction'''
    mycursor.execute(drop_query)
    mycursor.execute('''CREATE TABLE if not exists top_transaction (States varchar(50),
                                                                    Years int,
                                                                    Quaters int,
                                                                    pincodes int,
                                                                    Transaction_count bigint,
                                                                    Transaction_amount bigint)''')

    for index,row in toptransactlist.iterrows():
        insert_query5 = '''INSERT INTO top_transaction (States, Years, Quaters, Pincodes, Transaction_count, Transaction_amount)
                                                        values(%s,%s,%s,%s,%s,%s)'''
        values = (row["States"],
                row["Years"],
                row["Quaters"],
                row["Pincodes"],
                row["Transactioncount"],
                row["Transactionamount"])
        mycursor.execute(insert_query5,values)
        mydb.commit()

#top user table
def top_user_table():
    drop_query = '''drop table if exists top_user'''
    mycursor.execute(drop_query)
    mycursor.execute('''CREATE TABLE if not exists top_user (States varchar(50),
                                                        Years int,
                                                        Quaters int,
                                                        Pincodes int,
                                                        RegisteredUser bigint
                                                        )''')

    for index,row in topuser.iterrows():
        insert_query6 = '''INSERT INTO top_user (States, Years, Quaters, Pincodes, RegisteredUser)
                                                values(%s,%s,%s,%s,%s)'''
        values = (row["States"],
                row["Years"],
                row["Quaters"],
                row["Pincodes"],
                row["Registereduser"])
        mycursor.execute(insert_query6,values)
        mydb.commit()       


aggretransaction.to_csv('aggregated_transaction.csv',index=False)
aggreuser.to_csv('aggregated_user.csv',index=False)
maptranshist.to_csv('map_transaction.csv',index=False)
mapuserlist.to_csv('map_user.csv',index=False)
toptransactlist.to_csv('top_transaction.csv',index=False)
topuser.to_csv('top_user.csv',index=False)


def state_list():
    mydb = pymysql.connect(host="localhost",user="root",password="Chunnu@123",database="phonepay")
    mycursor=mydb.cursor() 
    mycursor.execute(f"""select distinct States 
                        from aggregated_transaction
                        order by States asc;""")
    data = mycursor.fetchall()
    original_state = [i[0] for i in data]
    return original_state

def year_list():
    mydb = pymysql.connect(host="localhost",user="root",password="Chunnu@123",database="phonepay")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT distinct Years FROM aggregated_transaction order by Years asc;")
    data = mycursor.fetchall()
    data = [i[0] for i in data]
    return data
def quarter_list():
    mydb = pymysql.connect(host="localhost",user="root",password="Chunnu@123",database="phonepay")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT distinct Quaters FROM aggregated_transaction order by Quaters asc;")
    data = mycursor.fetchall()
    data = [i[0] for i in data]
    return data
def get_transaction_type():
    mydb = pymysql.connect(host="localhost",user="root",password="Chunnu@123",database="phonepay")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT distinct Transactiontype FROM aggregated_transaction;")
    data = mycursor.fetchall()
    data = [i[0] for i in data]
    return data
def aggregate_trans_avg(aggregated_transaction):
    data = []
    for i in range(0, len(aggregated_transaction)):
        averg = aggregated_transaction.iloc[i]["Transactionamount"] / aggregated_transaction.iloc[i]["Transactioncount"]
        data.append(averg)
    return data
def get_map_transaction():
    mycursor.execute("SELECT * FROM map_transaction;")
    data = mycursor.fetchall()
    d = pd.DataFrame(data, columns=("States","Years","Quaters","Districts","Transactioncount","Transactionamount"))
    return d
def get_map_users():
    
    mycursor.execute("SELECT * FROM map_user;")
    data = mycursor.fetchall()
    d = pd.DataFrame(data, columns=("States", "Years", "Quaters", "Districts", "Registereduser", "Appsopen"))
    return d



def get_agg_use():
    mycursor.execute("SELECT * FROM phonepay.aggregated_user;")
    data=mycursor.fetchall()
    dm=pd.DataFrame(data, columns=("States", "Years", "Quaters", "Brands", "Transactioncount", "Percentage"))
    return dm



def user_trans_avg(map_user):
    data = []
    for i in range(0, len(map_user)):
        avg = map_user.iloc[i]["Appsopen"] / map_user.iloc[i]["Registereduser"]
        data.append(avg)
    return data

def new_frame(v):
    i = [i for i in range(1, len(v)+1)]
    data = pd.DataFrame(v.values, columns=v.columns, index=i)
    return data

#STREAMLIT
st.set_page_config(page_title= "Phonepe Pulse Data Visualization | By Vitasta Singh",
                   
                   layout= "wide",
                   initial_sidebar_state= "expanded")

st.title(":blue[Phonepe Pulse Data Visualization]")

with st.sidebar:
    st.header(":wave: :violet[**Hello! Welcome to the dashboard**]")
    
    selected = option_menu(None,
                            options=["Home","India","Transactions Insights","User Insights"],
                            icons=["house","india", "cash-coin", "bi-people"],
                            default_index=0,
                            orientation="horizontal",
                            styles={"container": {"width": "90%"},
                                    "options": {"margin": "10px"},
                                    "icon": {"color": "green", "font-size": "24px"},
                                    "nav-link": {"font-size": "20px", "text-align": "center", "margin": "15px", "--hover-color": "#6F36AD"},
                                    "nav-link-selected": {"background-color": "#6F36AD"}})
if selected == "Home":
    
    
    st.header(":violet[📱PHONEPe]  INDIA'S Most Trusted Payment Gateway")
    st.subheader("DOMAIN: :green[Fintech]")
    st.subheader(":green[TECHNOLOGIES-USED]")
    st.markdown("Github Cloning, Python, Pandas, MYSQL, Streamlit, and Plotly")
    st.subheader("OVERVIEW")
    st.markdown("PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")

    st.write("****FEATURES****")
    st.write("****Credit & Debit card linking****")
    st.write("****Bank Balance check****")
    st.write("****Money Storage****")
    st.write("****PIN Authorization****")
    st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
if selected == "India":
    MAP= st.selectbox("select your MAP",("Click to select","Total transactions","Registered Users","Apps Open"))
    def get_aggregated_tran():
            mycursor.execute( "SELECT * FROM phonepay.aggregated_transaction;")
            data = mycursor.fetchall()
            df = pd.DataFrame(data, columns=("States", "Years", "Quaters", "Transactiontype", "Transactioncount", "Transactionamount"))
            return df
    if MAP=='Total transactions':
            total_trans=get_aggregated_tran()
            total_trans=total_trans.groupby(["States"])[["Transactioncount"]].sum().reset_index()
            fig = px.choropleth(total_trans,
                                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='States',
                                color='Transactioncount',
                                color_continuous_scale="Viridis",
                                title="Transactions state wise",
                                        height=1000, width=1200)
            fig.update_geos(fitbounds='locations', visible=False)
            st.plotly_chart(fig)      
    if MAP =="Registered Users":
        def get_map_users():    
            mycursor.execute("SELECT * FROM phonepay.map_user;")
            data = mycursor.fetchall()
            d = pd.DataFrame(data, columns=("States", "Years", "Quaters", "Districts", "Registereduser", "Appsopen"))
            return d
        totaluser = get_map_users()
        totaluser = totaluser.groupby(["States"])[["Registereduser", "Appsopen"]].sum().reset_index()
        data =state_list()
        fig = px.choropleth(totaluser,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='States',
                            color='Registereduser',
                            color_continuous_scale="Reds",
                            title="Registered Users state wise",
                                    height=1000, width=1200)
        fig.update_geos(fitbounds='locations', visible=False)
        st.plotly_chart(fig)
    if MAP=='Apps Open':
        def get_map_users():    
            mycursor.execute("SELECT * FROM phonepay.map_user;")
            data = mycursor.fetchall()
            d = pd.DataFrame(data, columns=("States", "Years", "Quaters", "Districts", "Registereduser", "Appsopen"))
            return d
        totaluser = get_map_users()
        totaluser = totaluser.groupby(["States"])[["Registereduser", "Appsopen"]].sum().reset_index()
        fig = px.choropleth(totaluser,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='States',
                            color='Appsopen',
                            color_continuous_scale="Greens",
                            title="App opens state wise",
                                    height=1000, width=1200)
        fig.update_geos(fitbounds='locations', visible=False)
        st.plotly_chart(fig)    
if selected == "Transactions Insights":
    def get_aggregated_tran():
            mycursor.execute( "SELECT * FROM phonepay.aggregated_transaction;")
            data = mycursor.fetchall()
            df = pd.DataFrame(data, columns=("States", "Years", "Quaters", "Transactiontype", "Transactioncount", "Transactionamount"))
            return df
    with st.container():       
        st.markdown(":black[TRANSACTIONS INSIGHTS]")
        col1, col2, col3 = st.columns(3)
        # select box
        with col1:
            state = st.selectbox(label="Select the state",
                                 options=state_list(), index=0)
        with col2:
            year = st.selectbox(label="Select the year",
                                options=year_list(), index=0)
        with col3:
            quarter = st.selectbox(label="Select the Quarter", 
                                   options=quarter_list(), index=0)             
            

        
        
        df_agg_tran = get_aggregated_tran()
        avg_value = aggregate_trans_avg(aggretransaction)
        avg_value = pd.DataFrame(avg_value, columns=["avg_value"])
        df_av = pd.concat([df_agg_tran, avg_value], axis=1)
        v = df_av[(df_av["Years"] == year) & (df_av["Quaters"] == quarter)& (df_av["States"] == state)]
        total_transactions = v["Transactioncount"].sum()
        total_transaction_amount =v["Transactionamount"].sum()
        total_avg=v["avg_value"].sum()
        col1,col2,col3=st.columns(3)
        with col1:
            st.markdown(":black[All PhonePe transactions (UPI + Cards + Wallets)]")
            st.write(total_transactions)
        with col2:
            st.markdown(":black[Total payment value]")
            st.write( total_transaction_amount)
        with col3:
            st.markdown(":black[Avg. transaction value]")
            st.write(total_avg)
                        
        plt.figure(figsize=(12, 5))
        fig = px.pie(v, values='Transactionamount', names='Transactiontype', title='Pie Chart for Transaction Types',
            hover_data=['Transactioncount', 'avg_value'])

        fig.update_traces(textinfo='percent+label', pull=[0.1] * len(v['Transactiontype']))
        st.write(fig)

        st.markdown("")
        new_v = new_frame(v)
        st.table(new_v)

        col1, col2 = st.columns(2)
            
        with col1:
            year_df = st.selectbox(label="Select year", options=(2018, 2019, 2020, 2021, 2022, 2023), index=0)

        with col2:
            transaction_type = st.selectbox(label="Select the transaction type", options=get_transaction_type(), index=0)

        df_agg_total = get_aggregated_tran()
        df_agg_total = df_agg_total.groupby(["States", "Years", "Transactiontype"])[["Transactioncount", "Transactionamount"]].sum().reset_index()
        q = df_agg_total[(df_agg_total["Years"] == year_df) & (df_agg_total["Transactiontype"] == transaction_type)]

        fig = px.bar(q, x='States', y='Transactioncount',hover_data=['States', 'Transactioncount'], height=500, title="Transaction count state wise")
        st.write(fig)


        df_agg_total = get_aggregated_tran()
        df_agg_total = df_agg_total.groupby(["States", "Years", "Transactiontype"])[["Transactioncount", "Transactionamount"]].sum().reset_index()
        q = df_agg_total[(df_agg_total["Years"] == year_df) & (df_agg_total["Transactiontype"] == transaction_type)]

        fig = px.bar(q, x='States', y='Transactionamount',hover_data=['States', 'Transactionamount'], height=500, title="Transaction Amount state wise")
        st.write(fig)

        st.markdown("")
        new_v = new_frame(q)
        st.table(new_v)   


        st.markdown("#### Top 10 DISTRICTS")
        year_d= st.selectbox(label="Select year for the district wise data", options=(2018, 2019, 2020, 2021, 2022, 2023), index=0)
            
        st.markdown("#### Top 10 DISTRICTS for Transaction Count wise")
        df = get_map_transaction()
        df = df.groupby(["Years", "Districts"])[["Transactioncount", "Transactionamount"]].sum().reset_index()
        k = df[df["Years"] == year_d]
        c = k.sort_values(by=["Transactioncount"],ascending=False).head(10)[["Districts", "Transactioncount"]]
        c_df = new_frame(c)
        fig = px.pie(c_df, values='Transactioncount', names='Districts', title=f'Top 10 Districts for Year {year_d}')

# Display the pie chart
        st.plotly_chart(fig, use_container_width=True)

        def get_top_transaction():
            mycursor.execute("SELECT * FROM top_transaction;")
            data = mycursor.fetchall()
            d = pd.DataFrame(data, columns=("States","Years","Quaters", "pincodes", "Transaction_count","Transaction_amount"))
            return d


        st.markdown("#### Top 10 postalcodes")
        year_df_pc = st.selectbox(label="Select year for the postal code data", options=(2018, 2019, 2020, 2021, 2022, 2023), index=0)
        st.markdown("#### Top 10 postalcodes for Transaction Count wise")
        df = get_top_transaction()
        df = df.groupby(["Years", "pincodes"])[["Transaction_count", "Transaction_amount"]].sum().reset_index()
        k = df[df["Years"] == year_df_pc]
        c = k.sort_values(by=["Transaction_count"],ascending=False).head(10)
        c = c[["Years", "pincodes", "Transaction_count"]]
        c_df = new_frame(c)
        st.table(c_df) 

        st.markdown("#### Top 10 States")
        year_df_State = st.selectbox(label="Select year for the state wise data", options=(2018, 2019, 2020, 2021, 2022, 2023), index=0)

        st.markdown("#### Top 10 States for Transaction Count wise")
        df = get_agg_use()
        df = df.groupby(["Years", "States"])[["Transactioncount", "Percentage"]].sum().reset_index()
        k1 = df[df["Years"] == year_df_State]
        c1 = k1.sort_values(by=["Transactioncount"],ascending=False).head(10)[["States","Transactioncount"]]
        
        c1_df = new_frame(c1)
        fig = px.pie(c1_df, values='Transactioncount', names='States', title=f'Top 10 States for Year {year_df_State}')

# Display the pie chart
        st.plotly_chart(fig, use_container_width=True)

if selected == "User Insights":
    
    st.markdown("#### :black[USERS INSIGHTS]")
    col1, col2, col3 = st.columns(3)
    with col1:
        user_state = st.selectbox(label="Select the state users", options=state_list(), index=0)
        
    with col2:
        user_year = st.selectbox(label="Select the year users",options=year_list(), index=0)
         
    with col3:
        user_quarter = st.selectbox(label="Select the Quarter users", options=quarter_list(), index=0)
    def get_agg_use():
        mycursor.execute("SELECT * FROM phonepay.aggregated_user;")
        data=mycursor.fetchall()
        dm=pd.DataFrame(data, columns=("States", "Years", "Quaters", "Brands", "Transactioncount", "Percentage"))
        return dm
       
    
    user_df = get_agg_use()
    user = user_df[(user_df["States"] == user_state) & (user_df["Years"] == user_year) & (user_df["Quaters"] == user_quarter)]
    User_Count=user["Transactioncount"].sum()
    User_Percentage=user["Percentage"].sum()
    col1,col2=st.columns(2)
    with col1:
        st.markdown("User Count")
        st.write(User_Count)
    with col2:
        st.markdown("User Percentage")
        st.write(User_Percentage)
    
    pie_fig = px.pie(user, names="Brands", values="Transactioncount",title="Pie Chart for Users Brands")
    st.write(pie_fig)
      
    c_df = new_frame(user)
    st.table(c_df)

    total_state = st.selectbox(label="Select a state",options=state_list(), index=10)
    total_user = get_map_users()
    total_user = total_user.groupby(["States", "Years"])[ ["Registereduser", "Appsopen"]].sum().reset_index()
    to = total_user[total_user["States"] == total_state][1:]
    
    col1, col2 = st.columns(2)

    with col1:    
        fig = px.bar(to, x='Years', y='Registereduser', width=500, color="Years",title="Year wise Registered Users")
        st.write(fig)

    with col2:

        fig = px.bar(to, x='Years', y='Appsopen', width=500, color="Years", title="Year wise App opens")
        st.write(fig)

    st.markdown("")
    st.markdown("")
    to_df = new_frame(to)
    st.table(to_df)

    
    
        











