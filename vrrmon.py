from flask import Flask
from VRRMon import api

'''

 __      _______  _____  __  __             
 \ \    / /  __ \|  __ \|  \/  |            
  \ \  / /| |__) | |__) | \  / | ___  _ __  
   \ \/ / |  _  /|  _  /| |\/| |/ _ \| '_ \ 
    \  /  | | \ \| | \ \| |  | | (_) | | | |
     \/   |_|  \_\_|  \_\_|  |_|\___/|_| |_|


'''

app = Flask(__name__)
api_container = [api.Api(0)]

api_container[0].fetch()


@app.route('/')
def index():
    return ""


#   if __name__ == '__main__':
    #   app.run()

