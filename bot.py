#!/usr/bin/python
# -*- coding: utf-8 -*-
import Skype4Py
from random import choice
import re
skype = Skype4Py.Skype()
print("=====PIDORA OTVET=====")
print("Это приложение будет отвечать Пидора ответ! на все нет, которые напишут вам, будь то личное сообщение или конференция. Если вы переписываетесь с начальником или мамой, лучше отключите это приложени.")


def OnAttach(status):
    print 'API attachment status: ' + skype.Convert.AttachmentStatusToText(status)
    if status == Skype4Py.apiAttachAvailable:
        skype.Attach()

    if status == Skype4Py.apiAttachSuccess:
       print('***************************************')


global bot
bot = 'on'
q = re.compile(u'Кря, скажи, .+?\?')
calc = re.compile('-?\d+(,|\.)?\d*(\+|\*|-|/)-?\d+(,|\.)?\d*')
def OnMessageStatus(Message, Status):
    global bot
    global q
    if Status == 'RECEIVED':
        print(Message.FromDisplayName + ': ' + Message.Body)
        if bot == 'on':
            if Message.Body == u'нет' or Message.Body == u"Нет" or Message.Body == u"Нет!" or Message.Body == u"нет!" or Message.Body == u"нет." or Message.Body == u"Нет." or Message.Body == u"НЕТ":
                Message.Chat.SendMessage("Пидора ответ!")
            if Message.Body == u'триста' or Message.Body == "300":
                Message.Chat.SendMessage("Отсоси у тракториста!") 
            if Message.Body == u'Я не понял, повтори, пожалуйста':
                Message.Chat.SendMessage("Я не понял, повтори, пожалуйста") 
            if Message.Body == u'ясно':
                Message.Chat.SendMessage("понятно") 
            if Message.Body == u'понятно':
                Message.Chat.SendMessage("ясно") 
            if Message.Body == u'проиграл':
                Message.Chat.SendMessage("C тобой никто не играл, петушок.") 
            if Message.Body == u'Кря, кикни жа':
                Message.Chat.SendMessage("/kick zha.nya") 
            if Message.Body == u'Кря, добавь жа':
                Message.Chat.SendMessage("/add zha.nya") 
            if Message.Body == u'Кря, кикни рашота':
                Message.Chat.SendMessage("/kick kucakykylol") 
            if Message.Body == u'Кря, добавь рашота':
                Message.Chat.SendMessage("/add kucakykylol") 
            if re.match(q, Message.Body):
                answers = [u'Да', u'Нет', u'Это не важно', u'Спок, бро', u'Толсто', u'Да, хотя зря', u'Никогда', u'100%', u'1 из 100', u'Спроси еще разок']
                Message.Chat.SendMessage(choice(answers)) 
            if re.match(calc, Message.Body):
                Message.Chat.SendMessage(eval(re.search(calc, Message.Body).group()))
            if Message.Body == u'Кря, справка':
                Message.Chat.SendMessage("Кря-бот версии ебал твою мамашу:\nнет, Нет, НЕТ, нет!, нет. Нет. Нет! > Пидора ответ\nтриста, 300 > Отсоси у тракториста\nясно, Ясно > Понятно\nпонятно, Понятно > Ясно\nпроиграл, Проиграл > С тобой никто не играл, петушок\nВопросы по шаблону Кря, скажи, *?  > Ответы сакрального оленя\n") 
    if Status == 'READ':
        pass
    if Status == 'SENT':
        print('Myself ' + Message.Body)
        if Message.Body == u'Я медленно включаю бота':
            Message.Chat.SendMessage("===Бот включен") 
            bot = 'on'
        if Message.Body == u'Блядь, бот включен или нет?':
            Message.Chat.SendMessage(bot) 
        if Message.Body == u'Я медленно выключаю бота':
            Message.Chat.SendMessage("===Бот отключен") 
            bot = 'off'
        if Message.Body == u'Кря, кикни жа':
            Message.Chat.SendMessage("/kick zha.nya") 
        if Message.Body == u'Кря, добавь жа':
            Message.Chat.SendMessage("/add zha.nya") 
        if Message.Body == u'Кря, кикни рашота':
            Message.Chat.SendMessage("/kick kucakykylol") 
        if Message.Body == u'Кря, добавь рашота':
            Message.Chat.SendMessage("/add kucakykylol") 
        if re.match(q, Message.Body):
            answers = [u'Да', u'Нет', u'Это не важно', u'Спок, бро', u'Толсто', u'Да, хотя зря', u'Никогда', u'100%', u'1 из 100', u'Спроси еще разок']
            Message.Chat.SendMessage(choice(answers)) 
        if re.match(calc, Message.Body):
            Message.Chat.SendMessage(eval(re.search(calc, Message.Body).group()))

skype.OnAttachmentStatus = OnAttach
skype.OnMessageStatus = OnMessageStatus

print('***************************************')
print 'Connecting to Skype...'
skype.Attach()

Cmd = ''
while not Cmd == 'exit':
    Cmd = raw_input('')
