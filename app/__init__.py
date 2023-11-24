# -*- coding: utf-8 -*-
from fastapi import FastAPI
from config import STATIC_CONFIG


def create_app():
    app = FastAPI(title=STATIC_CONFIG.APP_NAME, docs_url=STATIC_CONFIG.DOCS_URL,
                  version=STATIC_CONFIG.VERSION, redoc_url=None)
    app.config = STATIC_CONFIG

    from . import extensions
    extensions.init_app(app)

    from . import modules
    modules.init_app(app)

    return app


