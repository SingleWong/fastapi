# -*- coding: utf-8 -*-

import uvicorn
from wsgi import app

if __name__ == '__main__':
    # uvicorn.run('app:create_app', host="127.0.0.1", port=8080, debug=True, reload=True)
    uvicorn.run(app, host="127.0.0.1", port=8080)
