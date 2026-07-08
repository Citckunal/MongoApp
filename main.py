import streamlit as st
import pymongo
import time
with st.spinner("Loading....."):
       time.sleep(5)
conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb=conn["ojt"]
my=mydb["user_info"]
st.title("🐍All the basic python code")
t1=st.text_input("Username")
t2=st.text_input("Password",type="password")
b1=st.button("🔑 SIGNIN")
valid=0
if b1:
       ans=my.find({"uname":t1,"password":t2})
       for i in ans:
              valid=valid+1
              st.session_state["username"]=i['uname']
              st.session_state["password"]=i['password']
              st.switch_page("pages/profile.py")
                             
       if valid==0:
              st.success("Invalid User Login Details")
       

