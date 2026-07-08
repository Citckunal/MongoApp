import streamlit as st
if st.session_state.get("username", False):
    st.write("You are safely inside the app!")
else:
       st.warning("First Login !!!")
       st.stop()
st.title("Prime Python Code")
n=st.slider("Pick a number",1,100)
f=0
for i in range(1,n+1):
       if n%i==0:
              f=f+1

if f==2:
       st.success("PRIME")
else:
       st.success("NOT PRIME")
