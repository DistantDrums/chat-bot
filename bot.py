#!/usr/bin/python2
# -*- coding: utf-8 -*-
import Skype4Py
import re
import commands
from commands import *
skype = Skype4Py.Skype()
bot = 'on' #Статус бота on/off
q = re.compile(u'Кря, скажи, .+?\?') #регэксп для шаблона Кря, скажи, *?
addRegExp = re.compile(u'Кря, когда кто-то скажет ".+?", отвечай ".+?"')

for i in RegExp.keys(): #Компилируем регэкспы чтобы быстрее работало
    q = re.compile(i)
    CompiledRegExp[i] = q
    
def OnAttach(status):
#Автоматически переподключаемся, если вдруг чего случилось
    print 'API attachment status: ' + skype.Convert.AttachmentStatusToText(status)
    if status == Skype4Py.apiAttachAvailable:
        skype.Attach()

    if status == Skype4Py.apiAttachSuccess:
       print('***************************************')

def AddNewRule(string):
    a = re.findall(u'".+?"', string)
    query = a[0][1:-1]
    response = a[1][1:-1]
    Commands[query] = response
    with open('commands.py', 'r+') as f:
        f.seek(-2, 2)
        result = "    u'" + query + "' : u'" + response + "',\n\n}"
        f.write(result.encode('utf-8'))

def OnMessageStatus(Message, Status):
    global bot
    if Status == 'RECEIVED':
        print(Message.FromDisplayName + ': ' + Message.Body)
        if Message.Body == u'Кря, выключи бота!':
            bot = 'off'
            Message.Chat.SendMessage('(finger)')
        if Message.Body == u'Кря, включи бота!':
            bot = 'on'
            Message.Chat.SendMessage('(drunk)')
        if bot == 'on':
            for i,e in RegExp.items():
                if re.match(CompiledRegExp[i], Message.Body): Message.Chat.SendMessage(e())
            if re.match(addRegExp, Message.Body):
                AddNewRule(Message.Body) #Это для добавления нового правила
                Message.Chat.SendMessage('Who are you to fucking lecture me?')
            for i,e in Commands.items():
                if Message.Body == i: Message.Chat.SendMessage(e)
            for i,e in UserCommands.items():
                if Message.Body == i: Message.Chat.SendMessage(e)

    if Status == 'READ':
        pass

    if Status == 'SENT': #только отправленные сообщения
        print('Myself ' + Message.Body)
        if re.match(addRegExp, Message.Body):
            AddNewRule(Message.Body) #Это для добавления нового правила
            Message.Chat.SendMessage('Понятно.')
        if Message.Body == u'Кря, выключи бота!':
            bot = 'off'
            Message.Chat.SendMessage('(finger)')
        if Message.Body == u'Кря, включи бота!':
            bot = 'on'
            Message.Chat.SendMessage('(drunk)')
        for i,e in Commands.items():
            if Message.Body == i: Message.Chat.SendMessage(e)
        if bot == 'on':
            for i,e in UserCommands.items():
                if Message.Body == i: Message.Chat.SendMessage(e)
        for i,e in RegExp.items():
            if re.match(CompiledRegExp[i], Message.Body): Message.Chat.SendMessage(e())

skype.OnAttachmentStatus = OnAttach
skype.OnMessageStatus = OnMessageStatus

print('***************************************')
print 'Connecting to Skype...'
skype.Attach()

Cmd = ''
while not Cmd == 'exit':
    Cmd = raw_input('')
