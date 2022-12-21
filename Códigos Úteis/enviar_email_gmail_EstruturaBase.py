
import pandas as pd
import yagmail #pip install yagmail
from pathlib import Path


meu_email = 'algumemail@servidor.com'
minha_senha = '123' ##A senha que será colocada aqui tem q ser criada através do App Password da google: https://myaccount.google.com/apppasswords
usuario = yagmail.SMTP(user=meu_email,password=minha_senha)


email_destino = 'algumemail@servidor.com'
assunto_email =  f'Titulo'
corpo_email = f'''
blablablablabla


Atencionsamente,
fulano de tal
'''
img = yagmail.inline(r"C:\Users\blablabla\local\past\arquivo.jpeg")

anexo = [r"C:\Users\blablabla\local\past\arquivo.jpeg",r"C:\Users\blablabla\local\past\arquivo.jpeg"]


usuario.send(
    to=email_destino,
    subject=assunto_email,
    contents=corpo_email,
    attachments=anexo
    
)
