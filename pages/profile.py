import streamlit as st

import pymongo
conn=pymongo.MongoClient("mongodb+srv://kunalg15_db_user:UchdhJoflEo7GMli@citcapp.mong26u.mongodb.net/?appName=CitcApp")#Set the connection with mongo database and our code
mydb=conn["ojt"]
my=mydb["user_info"]

@st.dialog("CHANGE PASSWORD")
def cp():
    t1=st.text_input("Enter the old password")
    t2=st.text_input("Enter the new password")
    if st.button("Change Password"):
        my.update_one({"password":t1},{"$set": {"password":t2}})
        st.success("Password Changed successfully")
        
        
    
    
#Login check
if st.session_state.get("username", False):
    st.write("You are safely inside the app!")
else:
       st.warning("First Login !!!")
       st.stop()

st.balloons()
c1,c2,c3,c4=st.columns(4)
st.title("🐍All the basic python code")
st.success(f"Welcome :{st.session_state['username']}")
if c1.button("Logout",use_container_width=True):
       del st.session_state["username"]
       st.switch_page("main.py")
if c2.button("See Profile",use_container_width=True):
       str1=st.session_state["username"]
       str2=st.session_state["password"]
       res=my.find({"uname":str1,"password":str2})
       for i in res:
           st.success(i["password"])
           st.success(i["mobile"])
           st.success(i["email"])
           st.success(i["dob"])
              
if c3.button("Change Password",use_container_width=True):
       cp()
if c4.button("AI Implemetion"):
    pass


