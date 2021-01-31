from Oddschecker.Event import *
import Oddschecker.Tools as tl

import pprint


pp = pprint.PrettyPrinter(indent=4)


class League:
    scheme = "https://"
    host = "www.oddschecker.com/us/"
    base_url = scheme + host

    def __init__(self, sport_url, event_class):
        # self.base_url = self.scheme + self.host + base_url
        self.sport_url = sport_url
        self.event_class = globals()[event_class]
        self.event_list = []

    # Add start and end dates
    # Not important since we can just take all the events as one
    def init_event_list(self) -> None:
        events_dict = tl.get_json_dict(self.base_url + self.sport_url + "?ajax=1")
        date_to_events_list_dict = {}
        for i in events_dict['data']['card']['matches']:
            date_to_events_list_dict[i['date']] = i['cards'][0]['data']
            if len(i['cards']) > 1:
                print("Cards in base_url > 1 length: " + self.base_url)

        # pp.pprint(date_to_events_list_dict)
        # total_event_list = []
        for key in date_to_events_list_dict.keys():
            event_list = []
            for event in date_to_events_list_dict[key]:
                # print(self.base_url)
                event_obj = self.event_class(event, self.base_url)
                self.event_list.append(event_obj)
                # event_list.append(event_obj)
            # date_to_events_list_dict[key] = event_list

        for i in self.event_list:
            print(i)
            break
        # pp.pprint(date_to_events_list_dict)
        # self.event_list = total_event_list


class NBA(League):

    """
    Market Names
    {
# "name": "4th Quarter Draw No Bet",
# "name": "4th Quarter Winner",
# "name": "Second Half Result",
# "name": "3rd Quarter Winner",
# "name": "1st Half Point Spread",
# "name": "3rd Quarter Draw No Bet",
"name": "Second Half Result",
"name": "Half Time",
"name": "Draw No Bet - 2nd Half",
"name": "Moneyline",
"name": "Draw No Bet - 1st Half",
"name": "4th Quarter Draw No Bet",
"name": "4th Quarter Winner",
"name": "3rd Quarter Winner",
"name": "3rd Quarter Draw No Bet",
"name": "2nd Quarter Draw No Bet",
"name": "2nd Quarter Winner",
"name": "1st Quarter Winner",
"name": "Including Draw",
"name": "Total Points",
"name": "Total Points Odd/Even",
"name": "1st Half Point Spread",
"name": "Point Spread"
}
    """
    market_to_line_class = {
        "Moneyline": "Moneyline",
        "Total Points": "TotalOverUnder",
        "Point Spread": "PointSpread"
    }

    def __init__(self):
        League.__init__(self, "basketball/nba", 'NBAEvent')


class NCAAB(League):
    def __init__(self):
        League.__init__(self, "basketball/ncaab", 'NCAABEvent')

