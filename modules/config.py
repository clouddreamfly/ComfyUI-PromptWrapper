import os
import json



# config
class Config:

    def __init__(self, path):

        self.config = {}
        with open(path, "r", encoding='utf-8') as fp:
            bom = fp.read(1)
            if bom != "\ufeff":
                fp.seek(0)

            self.config = json.load(fp)


    def __getattr__(self, key):

        return self.config[key] if key in self.config else None
            


def _load_config():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(script_dir, "../assets", "config.json")
    return Config(config_file)


# 读取配置
config = _load_config()

