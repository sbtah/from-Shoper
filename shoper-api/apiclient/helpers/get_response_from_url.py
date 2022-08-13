import time
import requests


def get_response_type_for_url(url):
    """
    Return an HTTP status response from tested URL.
    Will be used to check URLs at Shoper store.
    """

    url = f"{url}"
    response = requests.get(url)
    res = response.json()
    time.sleep(0.5)

    return res
