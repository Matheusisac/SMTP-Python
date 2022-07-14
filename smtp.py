import smtplib

remetente = 'Email do remetente'
recebidores = ['email do recebidor'] #Pode adicionar varios emails nessa variavel, em forma de lista

message = "From: <" + remetente + """>
To: <""" + str(recebidores) + """>
Subject: SMTP e-mail test

This is a test e-mail message.
"""


smtpObj = smtplib.SMTP('mail.domain.com', 587)
smtpObj.login(remetente, "password")
smtpObj.sendmail(remetente, recebidores, message)         
print ("Enviado com sucesso")
