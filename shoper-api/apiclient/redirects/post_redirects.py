import json
import time
import requests
from helpers.get_token import SHOPER_DOMAIN, TOKEN


def create_redirect(from_url, to_url):
    """
    https://shop.url/webapi/rest/redirects
    Create a redirect from relative URL
    to new absolute url.
    """

    data = json.dumps(
        {
            "route": from_url,
            "type": 0,
            "target": to_url,
        }
    )
    url = f"https://{SHOPER_DOMAIN}/webapi/rest/redirects"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.post(url, headers=headers, data=data)
    res = response.json()
    time.sleep(0.5)

    return res
