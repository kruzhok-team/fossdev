import logging
import sys
import structlog

FORMATTER_STRING = "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
FORMATTER = logging.Formatter(FORMATTER_STRING)

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    logger.addHandler(console_handler)
    return logger

def replace_user(_, __, event_dict):
    user = event_dict.get("user")
    if user:
        # we can access data base here for user_token
        # for now keep it fake
        user_token = "some_string_that_we_can_learn_username_from"
        event_dict["user"] = user_token
    return event_dict

def censor_password(_, __, event_dict):
    pw = event_dict.get("password")
    if pw:
        event_dict["password"] = "*CENSORED*"
    return event_dict

log = structlog.wrap_logger(
    get_logger("my_app_logger"),
    processors=[
        censor_password,
        replace_user,
        structlog.processors.JSONRenderer(indent=1, sort_keys=True),
    ],
)
log.warning("something", password="secret")
log.warning("something", user="Ivan")
