# from math import floor
'''
TODO:   ~ train index can be parametrized 
        ~ methods for preformatted


Sample api response:

{
    "error": null,          # Seems to be an error tag
    "preformatted": [],     # List consists of multiple List with l[0]=Line l[1]=Destination l[2]=countdown
    "raw":                  # List of dictionaries
    [
        {
            "countdown": "",                    # "2",
            "date": "",                         # "09.10.2017",
            "delay": "",                        # "0",
            "destination": "",                  # "Dortmund Dorstfeld Betriebshof",
            "info": "",                         # No sample response
            "key": "",                          # "963",
            "is_cancelled": None,               # 0,
            "line": "",                         # "U43",
            "lineref": {                        #
                "direction": "",                # "Dortmund Dorstfeld Betriebshof",
                "identifier": "",               # "dsw:36003: :R:s17",
                "mot": "",                      # "2",
                "name": "",                     # "U43",
                            "operator": "",     # "DSW U-Bahn",
                            "route": "",        # "DO-Wickede - Asseln - Brackel - Wambel - K\u00f6rne - Stadtmitte - Dorstfeld",
                            "type": "",         # "U-Bahn",
                            "valid": "",        # "Sommerfahrplan 2017 (11.06.2017 - 06.01.2018)"
                        },
                        "mot": "",              # "2",
                        "next_route": [],
                        "platform": "",         # "21",
                        "platform_db": None,    # 0,
                        "platform_name": "",    # No sample response
                        "prev_route": [],
                        "sched_date": "",       # "09.10.2017",
                        "sched_time": "",       # "23:20",
                        "time": "",             # "23:20",
                        "type": ""              # "U-Bahn"
        }
    ],
    "version": "0.07"                           # Version String
'''


class CallResult(object):

    def __init__(self, json):
        self.raw_data = json['raw']
        if len(self.raw_data) < 1:
            raise ValueError("Unknown City/Station.")
        self.preformatted_data = json['preformatted']
        self.train_index = len(json['raw'])-1
        self.current_index = 0

    def get_raw_data(self, index=0):
        return self.raw_data[index]

    def get_detail(self, keylist=None):
        output = {}
        if keylist is None:
            keylist = self.get_keys()
        for key in keylist:
            output[key] = self.raw_data[self.current_index][key]
        return output

    def get_keys(self):
        return self.raw_data[self.current_index].keys()
