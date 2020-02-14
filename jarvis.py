# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:50:41 2020

@author: benja
"""

class Jarvis(object):
    
    def __init__(self, api_key=None, database=None):
        self.api_key=api_key
        self.database=database #What is the database that Jarvis is logging to?
        self.training=False #Is jarvis currently training?
        self.current_action=None #Is there a current action type? 
        
        
    def startTrain(self):
        self.training=True
        return "Ok, I'm ready for training. What NAME should this ACTION be?"
    
    
    def stopTrain(self):
        self.training=False
        return "Ok I'm finished training"
      
        
    
    def respond(self, message):
        if self.training:
            if message['text']=='done':
                reply=self.stopTrain()
            else:
                reply=self.trainingSeq(message)
        elif message['text']=='training time':
            reply=self.startTrain()
        return reply
    
    
    
    
    def trainingSeq(self, message):
        if self.current_action:
            message['action']=self.current_action
            self.current_action=None
            reply=self.logData(message)
        else:
            self.current_action=message['text']
            reply=f"Ok lets call this action {self.current_action}"
        return reply

    
    
    
    def logData(self, message):
        '''Log Data to self.database'''
        #Do logging stuff
        return "Ok, I've got it! What else do you want to teach me?"
         
    
def test():
    '''Try talking to jarvis without website connection'''
    J=Jarvis()
    message={}
    print('This is a non web-based test of jarvis. Type in your commands here')
    
    while True:
        message['text']=input('\n') 
        if message['text'].lower()=='quit': 
            break
        reply=J.respond(message)
        
        print(reply)
        
if __name__=='__main__':
    test()