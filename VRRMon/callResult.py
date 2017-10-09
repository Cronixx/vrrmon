class CallResult(object):

    def __init__(self, json):
        self.data = {
            "preformatted": [],
            "countdown": "",        # "2",
            "date": "",             # "09.10.2017",
            "delay": "",            # "0",
            "destination": "",      # "Dortmund Dorstfeld Betriebshof",
            "info": "",             # No sample response
            "is_cancelled": None,   # 0,
            "key": "",              # "963",
            "line": "",             # "U43",
            "lineref": {            #
                "direction": "",    # "Dortmund Dorstfeld Betriebshof",
                "identifier": "",   # "dsw:36003: :R:s17",
                "mot": "",          # "2",
                "name": "",         # "U43",
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
