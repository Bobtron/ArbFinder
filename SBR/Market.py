# from pysbr import *
from SBR.Participant import Participant
from prettytable import PrettyTable


class Market:
    """
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
    def __init__(self, event_id: int, market_id: int, market_name: str):
        self.event_id = event_id
        self.market_id = market_id
        self.market_name = market_name
        # self.participant_map = {}
        self.participants = {}
        self.sportsbooks = set()

    def add_odd(self, odd_dict: dict):
        if odd_dict['participant'] not in self.participants.keys():
            # self.participant_map[odd_dict['participant id']] = odd_dict['participant']
            self.participants[odd_dict['participant']] = Participant(odd_dict['participant'])
        self.sportsbooks.add(odd_dict['sportsbook'])
        self.participants[odd_dict['participant']].add_odd(odd_dict)
        pass

    def pprint_table(self):
        sportsbooks_list = sorted(list(self.sportsbooks))
        table = PrettyTable(["Participant", "Best Odds", "Percentage", "Best Odds Sportsbook"] + sportsbooks_list)
        for participant in self.participants.keys():
            self.participants[participant].add_table_row(table, sportsbooks_list)

        print(table)
        print()

