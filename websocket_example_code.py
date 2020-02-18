url= 'https://github.com/websocket-client/websocket-client'

import requests
import json
from jarvis import Jarvis

J=Jarvis()
import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time

def load_token(filename):
    with open(filename) as f:
        return f.read()

def on_message(ws, message):
    message=json.loads(message)
    if message:
        if message.get('type',None)=='message': 
           print(message)
           reply_text=J.onMessage(message)
           if reply_text:
               reply=json.dumps({
                       "id": 1,
                       "type": "message",
                       "channel": message['channel'],
                       "text": reply_text})
               ws.send(reply)
    #except:
   #     print (message)
    
       

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
       pass
        # for i in range(3):
          #  time.sleep(1)
         #   ws.send("Hello %d" % i)
        #time.sleep(1)
        #ws.close()
        #print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    token=load_token('token2.txt')
    
    websocket.enableTrace(True)
    response=requests.get(f'https://slack.com/api/rtm.connect?token={token}&pretty=1').json()
    print(response)
    url=response['url'].replace('\/', '/')
    ws = websocket.WebSocketApp(url=url,
                             on_open= on_open,
                             on_message = on_message,
                             on_error = on_error,
                             on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

