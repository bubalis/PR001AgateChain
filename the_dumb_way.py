# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:56:30 2020

@author: benja
"""

from jarvis import Jarvis
import time
import requests

def load_token(filename):
    with open(filename) as f:
        return f.read()
    
def check_replies(url, bot_username):
    return [m for m in requests.get(url).json()['messages'] if m['user']!=bot_username]


def connect_and_monitor(token, channel="CU5V62WSZ", bot=Jarvis()):
    bot_username='UU5QAFSN4'
    url=f'https://slack.com/api/channels.history?token={token}&channel={channel}&pretty=1'
    list1=check_replies(url, bot_username)
    
    while True:
        list2=check_replies(url, bot_username)
        if len(list2)>len(list1):
            responses=list2[::-1][len(list1):]
            for response in responses:
                if response['text'].lower()=='quit':
                    return
                reply=bot.onMessage(response)
                if reply:
                    reply=reply.replace(' ', '%20')
                    requests.post(f'https://slack.com/api/chat.postMessage?token={token}&channel={channel}&text={reply}&pretty=1')
                
            list1=list2
        time.sleep(.5)

if __name__=='__main__':     
    token=load_token('token.txt')
    connect_and_monitor(token, channel="CU5V62WSZ", bot=Jarvis())