import logging

import coloredlogs

# logging.disable(logging.INFO)

FIELD_STYLES = dict(
    asctime=dict(color='blue'),
    hostname=dict(color='magenta'),
    levelname=dict(color='green'),
    filename=dict(color='magenta'),
    name=dict(color='blue'),
    threadName=dict(color='green')
)

LEVEL_STYLES = dict(
    debug=dict(color='blue'),
    info=dict(color='white'),
    warning=dict(color='yellow'),
    error=dict(color='cyan'),
    critical=dict(color='red')
)

# 使用coloredlogs设置日志的输出形式
coloredlogs.install(level="DEBUG",
                    fmt="[%(asctime)s] [%(filename)s:%(lineno)d] 【%(levelname)s】 %(message)s",
                    level_styles=LEVEL_STYLES,
                    field_styles=FIELD_STYLES)

# 使用彩色日志
logging.debug("这是一个debug消息")
logging.info("这是一个info消息")
logging.warning("这是一个warning消息")
logging.error("这是一个error消息")
logging.critical("这是一个critical消息")
