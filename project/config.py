import os
import pathlib
from typing import List, Union
from functools import lru_cache

class BaseConfig:
    SIO_MODE: str = "asgi"
    SIO_MOUNTPOINT: str = "/"
    SIO_CORS: Union[str, List[str]] = '*'

    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent

    celery_broker_url: str = os.environ.get("celery_broker_url", 'redis://127.0.0.1:6379/0')
    celery_result_backend: str = os.environ.get("celery_result_backend", 'redis://127.0.0.1:6379/0')


class DevelopmentConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass

@lru_cache()
def get_settings():
    config_cls_dict = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "testing": TestingConfig,
    }

    config_name = os.environ.get("FASTAPI_CONFIG", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls

settings = get_settings()