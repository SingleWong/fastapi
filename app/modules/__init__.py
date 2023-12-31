# -*- coding: utf-8 -*-

def init_app(app, **kwargs):
    from importlib import import_module

    for module_name in app.config.ENABLED_MODULES:
        import_module(f'.{module_name}', package=__name__).init_app(app, **kwargs)
