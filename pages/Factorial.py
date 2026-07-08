import streamlit as st
if st.session_state.get("username", False):
    st.write("You are safely inside the app!")
else:
       st.warning("First Login !!!")
       st.stop()
       
       
st.title("Factorial Python Code")
n=st.slider("Pick a number",1,100)
f=1
for i in range(1,n+1):
       f=f*i
st.success(f"Factoral of {n} Is {f}")
with st.expander("See The Python Code"):
    st.code('''
            import streamlit as st
            n=st.text_input("Enter a no")
            f=1
            for i in range(1,n+1):
                   f=f*i
            st.success(f"Factoral={f}")
            ''')
    

