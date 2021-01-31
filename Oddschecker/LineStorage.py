
class LineStorage:
    def __init__(self):
        pass


class TotalOverUnderStorage(LineStorage):
    def __init__(self):
        LineStorage.__init__(self)


class Moneyline(LineStorage):
    def __init__(self, odds_dict: dict):
        LineStorage.__init__(self)


class TotalPoints(LineStorage):
    def __init__(self, odds_dict: dict):
        LineStorage.__init__(self)


class PointSpread(LineStorage):
    def __init__(self, odds_dict: dict):
        LineStorage.__init__(self)
