import structlog
import logging

logger_structlog = structlog.get_logger()
logger_standard = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

logger_structlog.info(
    "Hello Pythonista!",
    key_id="1234",
    conference_name="EuroPython",
    talk_name="Can we deploy yet?",
)
logger_standard.info(
    "Hello Pythonista! Conference name %s, talk name %s, key_id = %s"
    % ("EuroPython", "Can we deploy yet?", "1234")
)
