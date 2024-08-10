"""Parse settings from .env file and set up `settings` object."""

import secrets
from typing import Annotated, Literal

from pydantic import AnyUrl, BeforeValidator, PostgresDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


def _parse_cors(v: str) -> list[str]:
    """Parse CORS (Cross-Origin Resource Sharing) string."""
    return [i.strip() for i in v.split(",")]


class Settings(BaseSettings):
    """Create Settings from .env file."""

    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True, extra="ignore")
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    DOMAIN: str = "localhost"
    ENVIRONMENT: Literal["development", "production"] = "development"

    @computed_field
    @property
    def SERVER_HOST(self) -> str:  # noqa: N802
        """Return URL ofserver host as HTTP or HTTPS."""
        # Use HTTPS for anything other than local development
        if self.ENVIRONMENT == "development":
            return f"http://{self.DOMAIN}"
        return f"https://{self.DOMAIN}"

    BACKEND_CORS_ORIGINS: Annotated[list[AnyUrl] | str, BeforeValidator(_parse_cors)] = []

    FIRST_SUPERUSER: str = "admin@example.com"
    FIRST_SUPERUSER_PASSWORD: str = "changeme"

    PROJECT_NAME: str = "No Project Name :("
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "postgres"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "changeme"

    LOGFIRE_TOKEN: str = "changeme"

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:  # noqa: N802
        """Create Postgres database URI."""
        return MultiHostUrl.build(
            scheme="postgresql+psycopg",
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
        )


settings = Settings()

# Check if unsafe defaults exist
if "changeme" in [settings.FIRST_SUPERUSER_PASSWORD, settings.POSTGRES_PASSWORD, settings.LOGFIRE_TOKEN]:
    msg: str = (
        "Do not use default values for secrets (passwords, tokens), please change all secrets with value of 'changeme'"
    )
    raise ValueError(msg)
