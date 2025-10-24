import json

class  SingletonConfig:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance =  super().__new__(cls)
            with open('../config.json', 'r') as file:
                data = json.load(file)
            cls._instance.log_level = data['log_level']
            cls._instance.data_path = data['data_path']
            cls._instance.report_path  = data['report_path']
            cls._instance.default_strategy = data['default_strategy']
        return cls._instance

