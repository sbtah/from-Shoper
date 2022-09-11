import time
from apiclient.helpers.logging import logging


def time_it(function):
    """
    Helper decorator used for calculating run time of certain functions.
    """

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = function(*args, **kwargs)
        t2 = time.time() - t1
        logging.info(f"{function.__name__}, ran in: {t2} seconds.")
        return result

    return wrapper
