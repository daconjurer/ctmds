from functools import lru_cache

from pydantic import Field

from ctmds.settings.api import APISettings
from ctmds.settings.base import CommonSettings


class AppSettings(CommonSettings):
    api: APISettings = APISettings()

    environment: str = Field(validation_alias="ENVIRONMENT", default="dev")
    project_name: str = "CTMDS (Commodity Trading Management System)"
    project_description: str = "A FastAPI-based API for commodity trading management."


@lru_cache(maxsize=1)
def get_app_settings() -> AppSettings:
    return AppSettings()
