import logging
import logging.config
import json
import os

if __name__ == '__main__':

    with open('logging\logging.json', 'rt') as f:
        config = json.load(f)

        logging.config.dictConfig(config)

        logger = logging.getLogger()
        logger.warning("warning message")