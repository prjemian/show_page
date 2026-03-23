"""Tsooyts (ցույց) — Electronic page display for church congregations."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("tsooyts")
except PackageNotFoundError:
    __version__ = "0.0.0"
