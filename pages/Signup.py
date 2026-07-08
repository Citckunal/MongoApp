import streamlit as st
import pymongo
conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")#Set the connection with mongo database and our code
mydb=conn["ojt"]#ojt is database on mongodb
my=mydb["user_info"]#user_info is a collection on mongodb
st.title("📝 S i g n U p")
t1=st.text_input("Username")
t2=st.text_input("Password",type="password")
t3=str(st.text_input("Mobile Number"))
t4=st.text_input("Email Id")
t5=st.date_input("DOB")
b1=st.button("SIGNUP")
if b1:
       my.insert_one({"uname":t1,"password":t2,"mobile":str(t3),"email":t4,"dob":str(t5)});
      
       st.success("✅ Sign Up Successfully")


