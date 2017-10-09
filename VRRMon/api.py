import configparser
import json
import requests
from VRRMon import callResult


class Api(object):
    '''
    Api Object

    TODO: Constructor with Config File

        def __init__(self, config_file):
            config = configparser.RawConfigParser()
            onfig.read(config_file)
        
    '''

    BASE_URI = ["https://vrrf.finalrewind.org/", "CITYARG", "/", "STATIONARG", ".json?frontend=json"]

    def __init__(self):
        self.resp_json = []
        self.call_results = []

    def fetch(self, city="Dortmund", station="Wickede S"):
        url = requests.get(self.build_url(city, station))
        response = json.loads(url.content.decode())
        self.resp_json.append(response)
        self.call_results.append(callResult.CallResult(response))

    def get_json_str(self, sort=True):
        if self.resp_json is None:
            return None
        if type(self.resp_json) is str:
            return self.resp_json
        else:
            return str(json.dumps(self.resp_json, sort_keys=sort))

    def print_json(self, sort=True, indents=4):
        if self.resp_json is None:
            return None
        if type(self.resp_json) is str:
            print(json.dumps(json.loads(self.resp_json), sort_keys=sort, indent=indents))
        else:
            print(json.dumps(self.resp_json, sort_keys=sort, indent=indents))
        return None

    def get_resp_json(self, index=-1):
        return self.resp_json[index]

    def get_resp_data(self, index=-1):
        return self.resp_data[index]

    @staticmethod
    def build_url(city, station):
        return Api.BASE_URI[0] + city + Api.BASE_URI[2] + station + Api.BASE_URI[4]