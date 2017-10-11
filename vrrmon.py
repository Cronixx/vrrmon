import configparser
from flask import Flask
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

config = configparser.ConfigParser()
config.read('./conf/conf.ini')
print(config.sections())
print(config.items())
print(config.values())

app = Flask(__name__)

api_container = [api.Api(0)]
api_container[0].fetch()


@app.route('/')
def index():
    return api_container[0].display()


if __name__ == '__main__':
   app.run()

