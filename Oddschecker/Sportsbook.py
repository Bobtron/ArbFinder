from typing import List

class Sportsbook:
    sb_names_to_code = {
        "DraftKings": "U6",
        "Fanduel": "U1",
        "Unibet": "UJ",
        "William Hill US": "E6",
        "BetMGM": "UG",
        "Borgata": "UR",
        "Bet365": "B3",
        "FOX Bet": "U4",
        "Pointsbet": "U7",
        "Play Sugar House": "U2",
        "888 US": "U5",
        "Bet America": "U3",
        "Resorts Casino": "U8"
    }

    def __init__(self):
        pass

    def get_ids(self, names_list: List[str]):
        return [self.sb_names_to_code[name] for name in names_list]
