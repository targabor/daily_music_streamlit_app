import streamlit as sl
import requests
import snowflake.connector
import re
import base64
import hashlib


regex = re.compile(
    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

sl.header('Schema Music')


def add_email_to_mailing_list(email: str):
    if email_is_valid(email) and email != 'example@example.com':
        email_bytes = email.encode('utf-8')
        encoded_email = base64.b64encode(email_bytes)
        hashed_email = hashlib.sha256(encoded_email).hexdigest()
        with con.cursor() as cur:
            cur.execute(
                "INSERT INTO CONSOLIDATED.subscribers (ID, EMAIL) VALUES (%s,%s);", (hashed_email, email))
            sl.write(f'subscribed with {email}')
    else:
        sl.write('please add a valid email address')


def email_is_valid(email: str):
    if re.fullmatch(regex, email):
        return True
    else:
        return False


sl.write('If you want to get weekly updates of #daily-music and get to know a bunch of fun stats, subscribe to the mailing list!')
email = sl.text_input('', value='example@example.com')
if sl.button('Subscribe'):
    con = snowflake.connector.connect(**sl.secrets["snowflake"])
    add_email_to_mailing_list(email)
    con.close()
