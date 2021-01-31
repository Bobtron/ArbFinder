# from pysbr import *
from SBR.Market import Market


class Event:
    """
    {   'country': 'England',
        'datetime': '2021-01-31T04:00:00-08:00',
        'description': 'Burnley FC@Chelsea FC',
        'event group': {   'alias': None,
                           'event group id': 994,
                           'name': 'Premier League'},
        'event id': 4210986,
        'event status': 'scheduled',
        'league id': 2,
        'location': 'London',
        'participants': [   {   'is home': False,
                                'participant id': 49218,
                                'source': {   'abbreviation': 'BUR',
                                              'location': '',
                                              'name': 'Burnley FC',
                                              'nickname': '',
                                              'short name': ''}},
                            {   'is home': True,
                                'participant id': 49249,
                                'source': {   'abbreviation': 'CFC',
                                              'location': '',
                                              'name': 'Chelsea FC',
                                              'nickname': '',
                                              'short name': ''}}],
        'scores': [],
        'season id': 25889,
        'sport id': 2,
        'stadium type': 'Undefined'}

        {   'american odds': 240,
            'datetime': '2021-01-23T17:39:57-08:00',
            'decimal odds': 3.4,
            'event': 'Fulham FC@Brighton & Hove Albion FC',
            'event id': 4210974,
            'market': 'Winner',
            'market id': 1,
            'participant': None,
            'participant full name': None,
            'participant id': 15145,
            'sportsbook': 'Bodog Sportsbook',
            'sportsbook alias': 'Bovada',
            'sportsbook id': 9,
            'spread / total': 0}
        """

    def __init__(self, event_dict: dict):
        """

        :param event_dict:
        :param market_ids:
        :param markets:
        """
        self.org_dict = event_dict
        self.datetime = event_dict['datetime']
        self.event_id = event_dict['event id']
        self.event_datetime = event_dict['datetime']
        self.event_desc = event_dict['description']
        self.participants = event_dict['participants']
        self.sport_id = event_dict['sport id']
        self.market_map = {}

    def add_odd(self, odd_dict: dict):
        """
        Adds this single odd into the list of markets for this event
        :param odd_dict:
        :return:
        """
        if odd_dict['market id'] not in self.market_map.keys():
            self.market_map[odd_dict['market id']] = Market(self.event_id, odd_dict['market id'], odd_dict['market'])
        self.market_map[odd_dict['market id']].add_odd(odd_dict)
        pass

    def pprint_markets(self, now):
        print("Event: " + self.event_desc)
        print("Event Datetime: " + self.event_datetime)
        print("Current Datetime: " + str(now))
        for market in self.market_map.keys():
            self.market_map[market].pprint_table()

