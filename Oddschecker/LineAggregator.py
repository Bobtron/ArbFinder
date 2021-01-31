from Oddschecker.Event import *
from Oddschecker import Tools as tl
from Oddschecker.Line import *
from Oddschecker.LineStorage import *
from typing import List
import pprint

pp = pprint.PrettyPrinter(indent=4)


class LineAggregator:
    def __init__(self, event: Event, market_to_line_class: dict, sportsbook_codes: List[str]):

        main_market = tl.get_json_dict(event.base_url + event.main_market_url + '?ajax=1')
        page_id = main_market['data']['page']['id']
        # print(page_id)

        all_markets = tl.get_json_dict(event.base_url + "view-all-markets/" + str(page_id))
        # pp.pprint(all_markets)

        market_to_id = {}

        for submarket in all_markets['bettingMarkets']:
            for market in submarket['markets']:
                market_to_id[market['name']] = market['id']
        # pp.pprint(market_to_id)

        line_storage = {}

        for market_name in market_to_line_class.keys():
            if market_name in market_to_id.keys():
                market_page = tl.get_json_dict(f'{event.base_url}subevent-market/{market_to_id[market]}?'
                                        f'currentPath={event.main_market_url}')

                line_class = globals()[market_to_line_class[market_name]]
                line_storage_class = globals()[market_to_line_class[market_name]]
                line_storage[market_to_line_class[market_name] + 'Storage'] = line_storage_class()
                for line in market_page['marketHolder']['market']['bets']:
                    new_line = line_class(line)
                    line_storage[market_to_line_class[market_name] + 'Storage'].add_line(new_line)



