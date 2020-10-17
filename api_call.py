from random import randint
from time import sleep
import schedule   # preciso baixar essa biblioteca
from twilio.rest import Client   # confirmar número no twilio
from twilio_information import *


group_of_messages = [
    'Opção de mensagem 1',
    'Opção de mensagem 2',
    'Opção de mensagem 3',
    'Opção de mensagem 4'
]

# Criar mais grupos de mensagens

def send_message(messages_list):
    account = twilio_account
    token = twilio_token
    client = Client (account, token)
    text = messages_list[randint(0, len(messages_list)-1)]

    client.messages.create(to=phone_number, from_=twilio_number, body=text)

schedule.every().day.at('7:00').do(send_message(group_of_messages))

while True:
    schedule.run_pending()
    sleep(30)