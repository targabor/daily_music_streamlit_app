import streamlit as sl
import requests
import snowflake.connector
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

sl.header('Schema Music')

def add_email_to_mailing_list(email: str):
    if email_is_valid(email) and email != 'example@example.com':
        with con.cursor() as cur:
        cur.execute(f"INSERT INTO CONSOLIDATED.subscribers VALUES ('{email}')")
        sl.write(f'subscribed with {email}')
    else:
        sl.write('please add a valid email address')
        
    

def email_is_valid(email: str):
    if re.fullmatch(regex, email):
      return true
    else:
      return false


email = sl.text_input('If you want to get weekly updates of #daily-music and get to know a bunch of fun stats, subscribe to the email list!', value='example@example.com')
if sl.button('Subscribe'):
    con = snowflake.connector.connect(**sl.secrets["snowflake"])
    add_email_to_mailing_list(email)

