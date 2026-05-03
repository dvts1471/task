import logging

from config import LOG_LEVEL


class Logger:
    _loggers: dict[str, logging.Logger] = {}

    def __init__(self, name: str = __name__, level: str = LOG_LEVEL) -> None:
        self.name = name
        if name not in self._loggers:
            self._loggers[name] = self._get_logger(name=name, level=level)

    @property
    def logger(self) -> logging.Logger:
        return self._loggers[self.name]

    def _get_logger(self, name: str = __name__, level: str = LOG_LEVEL) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if not logger.hasHandlers():
            logger.handlers.clear()
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def info(self, msg: str) -> None:
        self.logger.info(msg=msg)

    def debug(self, msg: str) -> None:
        self.logger.debug(msg=msg)

    def warning(self, msg: str) -> None:
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        self.logger.error(msg=msg)