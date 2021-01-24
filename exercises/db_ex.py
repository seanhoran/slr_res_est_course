import streamlit as st


def create_mail(text, subject, recipient, send=True):

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    mail.HtmlBody = text
    if send:
        mail.send()
    else:
        mail.save()

def db_ex():
  st.write("db exercise")
  import win32com.client as win32
  create_mail("Hello World!", "Test-Mail", "mail.adresss@gmail.de", send=False)





