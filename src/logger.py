import logging
from datetime import datetime
from pythonjsonlogger import jsonlogger
from src.config import settings


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get("timestamp"):
            now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            log_record["timestamp"] = now
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname


formatter = CustomJsonFormatter("%(timestamp)s %(level)s %(message)s %(module)s %(funcName)s")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)


logging.basicConfig(level=settings.LOG_LEVEL, handlers=[stream_handler])

logging.getLogger("fastapi").setLevel(settings.LOG_LEVEL)
logging.getLogger("uvicorn").setLevel(settings.LOG_LEVEL)
logging.getLogger("sqlalchemy.engine").setLevel(settings.LOG_LEVEL)


logger = logging.getLogger()
