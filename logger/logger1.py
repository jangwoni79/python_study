import logging

logger = logging.getLogger("name")

logger.setLevel(logging.INFO)

logger.info("Message")

logging.Formatter(
  fmt = None,     # 메시지 출력 형태. None일 경우 raw 메시지를 출력.
  datefmt = None, # 날짜 출력 형태. None일 경우 '%Y-%m-%d %H:%M:%S'.
  style = '%'     # '%', '{', '$' 중 하나. `fmt`의 style을 결정.
)
