import configparser
import json
import requests
from VRRMon import callResult
from VRRMon import formatter


class Api(object):
    '''
    TODO:       ~ configparser legt fest was für ein Formatter erstellt wird?
                    https://docs.python.org/3/library/configparser.html
                ~ YAGNI
    '''

    BASE_URI = ["https://vrrf.finalrewind.org/", "CITYARG", "/", "STATIONARG", ".json?frontend=json"]

    def __init__(self,
                 api_id,
                 city="Dortmund",
                 station="Wickede S"):

        self.current_callResult = None          # Last fetched response as api_object
        self.call_results = []                  # List of all call_results TODO: Shouldnt become bigger than 14
        self.city = city                        #  
        self.station = station                  # 
        self.api_id = api_id                    # ID to identify api object
        self.f = formatter.Formatter()          # Formatter object can handle callresults really nice
        self.call_url = "https://vrrf.finalrewind.org/{}/{}.json?frontend=json".format(self.city, self.station)

    def fetch(self):
        url = requests.get(self.call_url)
        response = json.loads(url.content.decode('utf-8'))
        self.current_callResult = callResult.CallResult(response)
        self.call_results.append(self.current_callResult)
        self.print_result()

    def display(self):
        return str(self.f.get_result(self.current_callResult))

    def current_callresult(self):
        return self.current_callResult

    def all_callresults(self):
        return self.call_results

    def print_result(self, index=-1):
        self.f.print_result(self.call_results[index])

    def set_new_formatter(self, new_f):
        if new_f.__class__ is formatter:
            self.f = new_f
