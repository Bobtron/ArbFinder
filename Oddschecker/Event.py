

class Event:
    def __init__(self, event_dict: dict, base_url: str):
        self.name = event_dict['name']
        self.start_time = event_dict['startTime']
        self.main_market_url = event_dict['mainMarketUrl']
        self.base_url = base_url

    def __str__(self):
        return f'Name: {self.name}\r\nStart Time: {self.start_time}\r\nMain Market URL: {self.main_market_url}\r\n'


class NBAEvent(Event):
    def __init__(self, event_dict: dict, base_url: str):
        Event.__init__(self, event_dict, base_url)
        self.home_team_full_name = event_dict['homeTeam']['fullName']
        self.home_team_short_name = event_dict['homeTeam']['shortName']
        self.away_team_full_name = event_dict['awayTeam']['fullName']
        self.away_team_short_name = event_dict['awayTeam']['shortName']

    def __str__(self):
        return Event.__str__(self) + f'Away: {self.away_team_short_name}\r\nHome: {self.home_team_short_name}'


class NCAABEvent(Event):
    def __init__(self, event_dict: dict, base_url: str):
        Event.__init__(self, event_dict, base_url)
