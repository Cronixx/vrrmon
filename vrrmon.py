from flask import Flask
from VRRMon import api
app = Flask(__name__)
vrrapi = api.Api()
vrrapi.fetch()
vrrapi.print_json()


@app.route('/')
def index():
    return ""


if __name__ == '__main__':
    app.run()

