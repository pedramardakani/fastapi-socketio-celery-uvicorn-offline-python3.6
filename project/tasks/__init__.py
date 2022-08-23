from typing import Union
from celery import shared_task
from project.config import settings

@shared_task
def say_hello(name: Union[None, str] = None) -> str:
    return f"Hello there {name if name else 'user'}!"
