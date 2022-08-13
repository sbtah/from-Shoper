import os
import time
import requests
from dotenv import load_dotenv
from apiclient.helpers.logging import logging


# Get private data fron .env variable
load_dotenv()
SHOPER_LOGIN = os.environ.get("SHOPER_LOGIN")
SHOPER_PASSWORD = os.environ.get("SHOPER_PASSWORD")
SHOPER_DOMAIN = os.environ.get("SHOPER_DOMAIN")


def get_token():
    """Generates fresh token from SHOPER API."""

    url_login = f"https://{SHOPER_DOMAIN}/webapi/rest/auth"
    assert SHOPER_DOMAIN, "Store domain not found, add .env file with store login data."

    try:
        response = requests.post(url_login, auth=(SHOPER_LOGIN, SHOPER_PASSWORD))
        response.raise_for_status()
        access_token = response.json().get("access_token")
        time.sleep(0.5)
    except requests.exceptions.Timeout:
        logging.error("Connection was timed out.")
        return None
    except requests.exceptions.ConnectionError:
        logging.error("Connection Error.")
        return None
    except requests.exceptions.HTTPError:
        logging.error("HTTPError was raised.")
        return None
    except Exception as e:
        logging.error(f"(get_token) Exception: {e}")
    else:
        return access_token


try:
    TOKEN = get_token()
except Exception as e:
    logging.error(f"Some other exception happend while getting token: {e}")
