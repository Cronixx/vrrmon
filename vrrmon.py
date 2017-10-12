import configparser
import zmq
import time
from VRRMon import api

'''

 __      _______  _____  __  __             
 \ \    / /  __ \|  __ \|  \/  |            
  \ \  / /| |__) | |__) | \  / | ___  _ __  
   \ \/ / |  _  /|  _  /| |\/| |/ _ \| '_ \ 
    \  /  | | \ \| | \ \| |  | | (_) | | | |
     \/   |_|  \_\_|  \_\_|  |_|\___/|_| |_|



TODO:       ~ Frontend --> Template bei google
            ~ Schnittstelle zum Messageversand an andere Programme  --> ZeroMQ
            ~ 
            ~ 
'''


ctx = zmq.Context()
socket = ctx.socket(zmq.REP)
socket.bind("tcp://*:5555")
config = configparser.ConfigParser()

config.read('conf/conf.ini')
print(config.sections())
print(config.items())
print(config)


if __name__ == '__main__':
    while True:
        try:
            # check for a message, this will not block
            requested = socket.recv_pyobj(flags=zmq.NOBLOCK)
            print("Received request: %s" % requested)
            #  Create new Api for request
            if len(requested) != 2:
                api_object = api.Api(config['Previous']['city'], config['Previous']['station'])
            else:
                api_object = api.Api(requested[0], requested[1])
            api_object.fetch()
            socket.send_pyobj(api_object.display())
        except ValueError as v:
            socket.send_pyobj(v)
        except zmq.Again as e:
            # No messages waiting to be processed
            print("No Client")
            pass
        #  Do some 'work'
        time.sleep(1)




