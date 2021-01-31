# from pysbr import *
from prettytable import PrettyTable

class Participant:
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
    def __init__(self, participant: dict):
        self.best_odd = 0
        self.best_percentage = 0
        self.best_odd_sportsbooks = []
        self.sportsbooks = set()
        self.sportsbooks_odds_map = {}
        self.participant = participant
        pass

    def add_odd(self, odd_dict: dict):
        self.sportsbooks.add(odd_dict['sportsbook'])
        self.sportsbooks_odds_map[odd_dict['sportsbook']] = odd_dict['decimal odds']
        if self.best_odd < odd_dict['decimal odds']:
            self.best_odd = odd_dict['decimal odds']
            self.best_odd_sportsbooks = [odd_dict['sportsbook']]
            self.best_percentage = 1.0 / odd_dict['decimal odds']
        elif self.best_odd == odd_dict['decimal odds']:
            self.best_odd_sportsbooks.append(odd_dict['sportsbook'])
        pass

    def add_table_row(self, table: PrettyTable, header: list):
        sportsbooks_list = sorted(list(self.sportsbooks))
        if header != sportsbooks_list:
            print("ERROR")
            print("Participant header = " + str(sportsbooks_list))
            print("Market header = " + str(header))
        row = [self.participant, self.best_odd, format(self.best_percentage * 100, '.3f'), ", ".join(self.best_odd_sportsbooks)]

        for sportsbook in sportsbooks_list:
            row.append(str(self.sportsbooks_odds_map[sportsbook]))
            if self.sportsbooks_odds_map[sportsbook] == self.best_odd:
                row[-1] = "->" + row[-1] + "<-"
        table.add_row(row)

