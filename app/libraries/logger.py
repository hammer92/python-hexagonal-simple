import logging
class Logger:
    def __init__(self, name: str):
        self._logging = logging.getLogger(name)
        self._logging.setLevel(logging.INFO)

    def info(self,  msg, *args, **kwargs):
        self._logging.info( msg, *args, **kwargs)

