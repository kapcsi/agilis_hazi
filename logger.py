import logging

our_logger = logging.getLogger(__name__)
file_handeler = logging.FileHandler("machines_log.log")
our_logger.setLevel(logging.INFO)
our_logger.addHandler(file_handeler)