"""Create Jinja2 template object."""

from typing import Any

from fastapi import Request
from fastapi.templating import Jinja2Templates
from fasthx import Jinja

from app.core.settings import frontend_settings


def frontent_settings_context(request: Request) -> dict[str, str]:  # noqa: ARG001
    """Return frontend_settings as Jinja context."""
    jinja_context: dict[str, Any] = {}
    jinja_context["frontend_settings"] = frontend_settings.model_dump()
    return jinja_context


jinja = Jinja(Jinja2Templates(directory="app/templates", context_processors=[frontent_settings_context]))
