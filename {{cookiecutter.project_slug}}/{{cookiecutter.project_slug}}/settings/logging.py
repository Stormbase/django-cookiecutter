"""
Settings related to logging. Typically imported from ``base.py``

"""

LOGGING = {
    "version": 1,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"  # noqa
        }
    },
    "disable_existing_loggers": True,
    "root": {"level": "INFO", "handlers": ["console"]},
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "null": {"class": "logging.NullHandler"},
    },
    "loggers": {
        # Application logger
        "{{cookiecutter.project_slug}}": {"level": "INFO", "propagate": True},
        "django": {"handlers": ["console"], "level": "ERROR", "propagate": True},
    },
}
