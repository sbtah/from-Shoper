import time
import requests


def get_response_type_for_url(url):
    """Return a response with from tested URL"""

    url = f"{url}"
    response = requests.get(url)
    res = response.status_code
    time.sleep(0.5)

    return res


print(
    get_response_type_for_url(
        "https://meowbaby.eu/pl/p/MeowBaby-Suchy-Basen-Okragly-bez-Pileczek-Czarny/273"
    )
)
