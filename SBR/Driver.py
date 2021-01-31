from pysbr import *
import pendulum
from SBR.League import League
from pprint import pprint

start = pendulum.now().add(days=1)#.strftime('%Y-%m-%d')

end = pendulum.now().add(days=8)#.strftime('%Y-%m-%d')

sb = Sportsbook()
# sb_ids = sb.ids(['Pinnacle', 'Bovada', 'Bookmaker', 'BetOnline', 'Heritage Sports', 'BetOnline', 'GTbets', 'YouWager',
#                  'Intertops', 'JustBet', 'WagerWeb', 'SportsBetting'])

print(sb.names)

sb_ids = list(sb.names.keys())

epl = EPL()

epl_league = League(epl)

epl_league.add_events(epl.market_ids(['moneyline']), sb_ids, start, end)

epl_league.pprint_events()

# pp = pprint.PrettyPrinter(indent=4)
#
# print(end)
#
# nfl = NFL()
# epl = EPL()
# sb = Sportsbook()
#
# print(nfl.market_names)
#
# print(sb.names)
#
# events = EventsByDateRange([epl.league_id], start, end)
#
# current_line = CurrentLines(events.ids(), epl.market_ids(['moneyline']), sb.ids(['Pinnacle', 'Bovada']))
#
# pp.pprint(events.list())
#
# print()
#
# pp.pprint(current_line.list(events))


