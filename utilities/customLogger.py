import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger("automationLogger")
        logger.setLevel(logging.DEBUG)

        # Prevent duplicate handlers
        if not logger.handlers:

            base_dir = os.path.abspath(os.curdir)
            log_dir = os.path.join(base_dir, "logs")

            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            log_file = os.path.join(log_dir, "automation.log")

            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter(
                '%(asctime)s:%(levelname)s:%(message)s',
                datefmt='%d/%m/%Y %I:%M:%S %p'
            )

            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger