import logging
import os


# logger = logging.basicConfig(filename='../log/logfile.log', format ='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                              level=logging.INFO, datefmt='%d/%m/%Y %I:%M:%S %p')
#
# log = logging.getLogger()
# log.error("This is an error")
# log.info("This is info")
# log.warning("This is warning")
class generateLog:

    def log(self):
        log_path = os.path.abspath("../log/logfile1.txt")
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        logging.basicConfig(filename="../log/logfile1.txt", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                     level=logging.INFO, datefmt='%d-%b-%y %I:%M:%S %p')
        logger = logging.getLogger()
        return logger

logger = generateLog()
log1 = logger.log()

log1.error("This is an error")
log1.info("This is an info")
log1.warning("This is warning")
