import streamlit as st

st.title("Student Login Form ")

with st.form("login_form"):

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    mobile = st.text_input("Mobile Number")

    gender = st.radio("Gender", ["Male", "Female", "Other"])
    course = st.selectbox("Course", ["BCA", "MCA", "BBA", "MBA"])

    Address = st.text_area("Address")
    agree = st.checkbox("I agree to the terms and conditions")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if not agree:
            st.warning("You must agree to the terms and conditions to submit the form.")
        else:
            st.success("Form submitted successfully!")
            st.write("Name:", name)
            st.write("age:", age)
            st.write("Email:", email)
            st.write("Mobile Number:", mobile)
            st.write("Gender:", gender)
            st.write("Course:", course)
            st.write("Address:", Address)

