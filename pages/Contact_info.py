import streamlit as st
from send_email import send_mail
st.header("Contact us")

with st.form(key="send_email"):

    st.text_input("Your Email", placeholder="Enter email...", key="email")
    st.multiselect("Select a topic :", ['Global warming', 'Ozone layer', 'God theory'], key="options")
    st.text_area("Text", placeholder="Write your thoughts...", key="message")
    button = st.form_submit_button("Submit")

    if button:

        email = st.session_state['email']
        options = st.session_state['options']
        text = st.session_state['message']
        print(options)
        message = ""
        for option in options:
            message = message + option + ", "

        message = message + "\n" + text
        message = f"""\
Subject: Email from {email}\n
From: {email}
{message}"""
        print(message)
        send_mail(email, message)


