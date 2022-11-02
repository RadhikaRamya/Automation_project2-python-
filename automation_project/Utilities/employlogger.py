import logging


def test_logdemo():
    # to get the name of the test case file name at runtime

    logger = logging.getLogger()

    # FileHandler class to set the location of log file

    fileHandler = logging.FileHandler('logfile.log')

    # formater class to set the format of log file

    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

    # obgect of FileHandler gets formatting info from setFormatter #method

    fileHandler.setFormatter(formatter)

    # logger object gets formatting path of log file info with adHandler method

    logger.addHandler(fileHandler)

    # setting lgging level to

    logger.setLevel(logging.INFO)

    # logger.setLevel(logging.ERROR)

    return logger
