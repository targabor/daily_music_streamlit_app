import streamlit as sl

sl.header('Schema Music coming soon...')

def add_mail_to_mailing_list(mail: str):
    # create snowflake connection
    # create statement and add mail
    # could add nickname to be more personal
    sl.write(mail)

def validate_mail(mail: str):
    pass

sl.write('If you want to get weekly updates of #daily-music and get to know a bunch of fun stats, subscribe to the email list!')


mail = sl.text_input('email', value='examle@example.com')
if sl.button('Subscribe'):
    add_mail_to_mailing_list(mail)

