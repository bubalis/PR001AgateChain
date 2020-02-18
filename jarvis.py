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
            if message['text'].lower()=='done':
                return self.stopTrain()
            else:
               return self.trainingSeq(message)
        elif message['text'].lower()=='training time':
            return self.startTrain()
        else:
            return None #Otherwise don't reply
    
    
    def filterMessages(self, message):
        '''Determine whether message should be responded to.
        Needs to actually be built, once we know what the api will be sending us.'''
        #if conditions
        return True
        #else: 
        return False
    
    def onMessage(self, message): #If there is a response, send it out!
        if self.filterMessages(message):
            return self.respond(message)
        
    
    def trainingSeq(self, message):
        '''Do training stuff'''
        if self.current_action: #if action is currently defined
            message['action']=self.current_action #assign  action to message dictionary
            self.current_action=None # delete action from class
            return self.logData(message) #log data
        else:
            self.current_action=message['text'].upper() #if action is not defined, define action as current message text.
            return f"Ok lets call this action {self.current_action}"

    
    def logData(self, message):
        '''Log Data to self.database. Message is a dictionary, 'action' and 'text' and 'time' are all keys.'''
        #Do logging stuff
        print(f'Message to log: {message}')
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
        reply=J.onMessage(message)
        if reply:
            print(reply)
        
if __name__=='__main__':
    test()