import logging

if __name__ == '__main__':
  test_logger = logging.getLogger("test") 
  test_logger.setLevel(logging.INFO)  

  stream_handler = logging.StreamHandler()
  test_logger.addHandler(stream_handler)

  file_handler = logging.FileHandler("test.log")
  test_logger.addHandler(file_handler)

  test_logger.debug("debug message")
  test_logger.info("info message")
  test_logger.warning("warning message")
  test_logger.error("error message")
  test_logger.critical("critical message")