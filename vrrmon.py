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




# configpath = 'conf/conf.ini'
# config = configparser.ConfigParser()
# config.read(configpath)

ctx = zmq.Context()
socket = ctx.socket(zmq.REP)
socket.bind("tcp://*:5555")

if __name__ == '__main__':
    while True:
        try:
            # check for a message, zmq.Again exception if no incoming message
            requested = socket.recv_pyobj(flags=zmq.NOBLOCK)
            print("Received request: %s" % requested)

            #  If valid request
            if len(requested) == 2:
                api_object = api.Api(requested[0], requested[1])
                api_object.fetch()
                socket.send_pyobj(api_object.display())
            else:
                socket.send_pyobj("Invalid Query: %s\nUSAGE: arg[0] = city, arg[1] = station" % requested)
        except ValueError as v:
            socket.send_pyobj("Invalid Query: %s " % str(v))
        except zmq.Again as e:
            # No messages waiting to be processed
            pass
        #  Do some 'work'
        time.sleep(1)




