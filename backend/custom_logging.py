# Custom Logger Using Loguru
import logging
import sys
from pprint import pformat
from pathlib import Path
from loguru import logger
from loguru._defaults import LOGURU_FORMAT
import json

config_path = Path(__file__).with_name("logging_config.json")


class InterceptHandler(logging.Handler):
    loglevel_mapping = {
        50: "CRITICAL",
        40: "ERROR",
        30: "WARNING",
        20: "INFO",
        10: "DEBUG",
        0: "NOTSET",
    }

    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except AttributeError:
            level = self.loglevel_mapping[record.levelno]

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        log = logger.bind(request_id="app")
        log.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


class CustomizeLogger:
    @classmethod
    def make_logger(cls):
        logger = cls.customize_logging()
        return logger

    @classmethod
    def customize_logging(cls):
        def format_record(record: dict) -> str:
            """
            Custom format for loguru loggers.
            Uses pformat for log any data like request/response body during debug.
            Works with logging if loguru handler it.

            Example:
            >>> payload = [{"users":[{"name": "Nick", "age": 87, "is_active": True}, {"name": "Alex", "age": 27, "is_active": True}], "count": 2}]
            >>> logger.bind(payload=).debug("users payload")
            >>> [   {   'count': 2,
            >>>         'users': [   {'age': 87, 'is_active': True, 'name': 'Nick'},
            >>>                      {'age': 27, 'is_active': True, 'name': 'Alex'}]}]
            """
            format_string = LOGURU_FORMAT

            if record["extra"].get("payload") is not None:
                record["extra"]["payload"] = pformat(
                    record["extra"]["payload"], indent=4, compact=True, width=88
                )
                format_string += "\n<level>{extra[payload]}</level>"

            format_string += "{exception}\n"
            return format_string

        logger.remove()

        logger.add(
            sys.stdout,
            enqueue=True,
            backtrace=True,
            level="INFO",
            format=format_record,
        )

        logger.add(
            str("./logs/access.log"),
            rotation="00:00",
            enqueue=False,
            backtrace=False,
            level="INFO",
            format=format_record,
        )

        logger.add(
            sys.stdout,
            enqueue=True,
            backtrace=True,
            level="ERROR",
            format=format_record,
        )
        logger.add(
            str("./logs/error.log"),
            rotation="00:00",
            enqueue=True,
            backtrace=True,
            level="ERROR",
            format=format_record,
        )

        logging.basicConfig(handlers=[InterceptHandler()], level=0)
        logging.getLogger().handlers = [InterceptHandler()]
        logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]
        for _log in ["uvicorn", "uvicorn.error", "fastapi"]:
            _logger = logging.getLogger(_log)
            _logger.propagate = False
        return logger.bind(request_id=None, method=None)


logger.remove()
logger = CustomizeLogger.make_logger()
