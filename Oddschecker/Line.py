



class Line:
    def __init__(self, odds_dict: dict):
        # print(dict)
        # print(type(self))



class TotalOverUnder(Line):
    def __init__(self, odds_dict: dict):
        Line.__init__(self, odds_dict)


class Moneyline(Line):
    def __init__(self, odds_dict: dict):
        Line.__init__(self, odds_dict)


class TotalPoints(Line):
    def __init__(self, odds_dict: dict):
        Line.__init__(self, odds_dict)


class PointSpread(Line):
    def __init__(self, odds_dict: dict):
        Line.__init__(self, odds_dict)
