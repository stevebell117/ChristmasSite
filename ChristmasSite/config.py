import yaml
import os

class Config(object):
    _path = None
    _data = {}

    def __init__(self):
        config_file = os.path.join(os.path.join(os.getcwd(), 'config'), 'config.yml')
        with open(config_file) as stream:
            try:
                self._data = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
    
    def __getattr__(self, attr):
        return self._data[attr]