url= 'https://github.com/websocket-client/websocket-client'

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
   # print(J.onMessage(message))
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    token=load_token('token.txt')
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://https://github.com/websocket-client/websocket-client", 
                                header={'token': token},
                                                 
                              on_open= on_open,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

