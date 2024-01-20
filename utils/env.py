import os
from dotenv import load_dotenv

class DotEnvLoader:
    _loaded = False

    @classmethod
    def load_env(cls, path):
        if not cls._loaded:
            load_dotenv(dotenv_path=path)
            cls._loaded = True

    @classmethod
    def get(cls, key, default=None) -> (str,bool):
        if not cls._loaded:
            return "", False
        return (os.getenv(key, default), True)
