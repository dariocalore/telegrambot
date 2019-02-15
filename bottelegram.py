import telepot

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    
    if content_type == 'text':
        
        txt = msg['text']
        if '/docente' in txt:
            bot.sendDocument(chat_id, 'http://www.polomanettiporciatti.gov.it/pvw/app/GRII0002/pvw_img.php?sede_codice=GRII0002&doc=2376192', caption=None, parse_mode=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
        elif '/studente' in txt:
            bot.sendDocument(chat_id, 'http://www.polomanettiporciatti.gov.it/pvw/app/GRII0002/pvw_img.php?sede_codice=GRII0002&doc=2376194', caption=None, parse_mode=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
        elif '/start' in txt:
            bot.sendMessage(chat_id, 'Scrivere il comando /docente per gli orari aggiornati dei docenti del porciatti, scrivere /studente per gli orari aggiornati degli studenti del porciatti, bot creato da Dario Calore')
        else:
            bot.sendMessage(chat_id, 'Mi spiace, non capisco')

TOKEN = 'YOUR TOKEN'

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

print 'Listening ...'

import time
while 1:
    time.sleep(10)
