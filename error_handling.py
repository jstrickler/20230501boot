import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

logging.basicConfig(
    handlers = [RotatingFileHandler(filename="charter2.log", maxBytes=500, backupCount=3)],
    format='%(levelname)s %(asctime)s %(filename)s %(message)s',
    datefmt='%x-%X',
)
logging.info("Program starting")

file_path = "DATA/wombats.txt"

try:
    with open(file_path) as file_in:
        for raw_line in file_in:
            print(raw_line.rstrip())
except (FileNotFoundError, PermissionError) as err:
    logging.exception(err)  # output to STDERR (not STDOUT)
except FileExistsError as err:
    logging.exception(err)
except Exception as err:
    logging.exception("I should log this...")

values = [0, 5, 18, 3.7, -6, 0, 48, 9, 0, 2]
for v in values:
    try:
        result = 100 / v
    except ZeroDivisionError as err:
        # print(err)
        continue  # skip this number
    else:
        print(result)

print("ALL DONE")

logging.info("program ending")