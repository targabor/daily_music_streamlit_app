import streamlit as sl
import requests
import snowflake.connector

sl.header('Schema Music')

def add_email_to_mailing_list(email: str):
    with con.cursor() as cur:
        cur.execute(f"INSERT INTO CONSOLIDATED.subscribers VALUES ('{email}')")
    sl.write(f'subscribed with {email}')

def validate_mail(mail: str):
    pass


email = sl.text_input('If you want to get weekly updates of #daily-music and get to know a bunch of fun stats, subscribe to the email list!', value='examle@example.com')
if sl.button('Subscribe'):
    con = snowflake.connector.connect(**sl.secrets["snowflake"])
    add_email_to_mailing_list(email)

