from Oddschecker.League import *
from Oddschecker.Sportsbook import *
from Oddschecker.LineAggregator import *
import Oddschecker.Tools as tl

nba = NBA()
nba.init_event_list()
sb = Sportsbook()

lines = LineAggregator(nba.event_list[0], nba.market_to_line_class, sb.get_ids(['DraftKings', 'FOX Bet']))