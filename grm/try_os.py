"""
    GRM package
    try_os... decorators
"""


import errno
import os
from flask import current_app
from time import sleep
from werkzeug.exceptions import InternalServerError, HTTPException


def try_os_io(function):
    """ Try OS io anything and try again if busy decorator

    :param function: Function to decorate
    :return: decorator
    """
    def wrapper(*args):
        """ Try os io wrapper """

        # get configs
        attempts = current_app.config.get("IO_ATTEMPTS", 10)
        sleep_for = current_app.config.get("IO_SLEEP_FOR", 0.2)

        # try to get os io attempts
        attempt = 0
        while attempt < attempts:

            attempt += 1
            try:
                # if no errors occurred, return from function
                return function(*args)

            except HTTPException as e:
                raise e

            except OSError as e:
                # try again only if file busy
                if e.errno not in [errno.ETXTBSY, errno.EBUSY]:
                    raise InternalServerError(f"OS ERROR (errno={e.errno}).\n{os.strerror(e.errno) if e.errno else ''}")
                # wait some time
                sleep(sleep_for)

        # if attempts is accomplished, raise exception
        raise InternalServerError("Exceeded the allowed number of server I/O attempts")

    return wrapper
