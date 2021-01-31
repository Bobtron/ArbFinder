import requests
from requests.exceptions import HTTPError
import pprint


def get_json_dict(url: str) -> dict:
    try:
        headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:86.0) Gecko/20100101 Firefox/86.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        # "Referer": "https://www.oddschecker.com/us/basketball/nba",
        "X-Requested-With": "XMLHttpRequest",
        "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
        "Expires": "Thu, 01 Jan 1970 00:00:00 GMT",
        "Pragma": "no-cache",
        "DNT": "1",
        "Connection": "keep-alive",
        "Sec-GPC": "1",
        "TE": "Trailers"
        }

        response = requests.get(url, headers=headers)

        # If the response was successful, no Exception will be raised
        # print(response.status_code)
        response.raise_for_status()

        return response.json()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print("Success")


# pp = pprint.PrettyPrinter(indent=4)
# response = get_json_dict("https://www.oddschecker.com/us/basketball/nba?ajax=1")
# response = get_json_dict("https://www.oddschecker.com/us/basketball/nba?ajax=1")

# pp.pprint(response['data']['card']['matches'][0])