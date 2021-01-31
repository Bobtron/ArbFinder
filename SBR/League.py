from pysbr import *
from SBR.Event import Event
import pendulum


class League:

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

    def __init__(self, league):
        self.league = league
        self.league_id = league.league_id
        self.sport_id = league.sport_id
        self.lines_last_updated = None
        self.events = {}

    def add_events(self, market_ids, sportsbook_ids, start_date, end_date=None):
        events = None
        if end_date == "":
            events = EventsByDate([self.league_id], start_date)
        else:
            events = EventsByDateRange([self.league_id], start_date, end_date)

        for event in events.list():
            self.events[event['event id']] = Event(event)

        current_lines = CurrentLines(events.ids(), market_ids, sportsbook_ids)
        self.lines_last_updated = pendulum.now()

        line_list = current_lines.list(events)

        for line in line_list:
            self.events[line['event id']].add_odd(line)

    def pprint_events(self):
        for event in self.events.keys():
            self.events[event].pprint_markets(self.lines_last_updated)
