
import logging

import time


logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
info_file_name = 'info-' + time.strftime(
    '%Y-%m-%d', time.localtime(time.time())) + '.log'
handler = logging.FileHandler(info_file_name)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")