def add(*args, **kwargs):
    result = 0

    for elem in list(args) + list(kwargs.values()):
        if isinstance(elem,(int,float,bool)):
            result += elem
        else:
            try:
                result += float(elem)
                continue
            except (ValueError, TypeError):
                pass


    return result


def devide(*args, **kwargs):
    result = 0

    for elem in args:
        result += elem

    for elem in kwargs.values():
        result += elem
    return result


import logging

logging.basicConfig(level=logging.DEBUG, filename='logs.log', filemode='w',
                    format="We have next logging message: %(asctime)s: %(levelname)s -%(message)s ")
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")
# #
try:
    logging.warning("cant devide by zero")
    print(10/0)
except Exception as ex:
    logging.exception(ex)
    logging.error(ex)
