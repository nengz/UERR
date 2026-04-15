import os
import json


class JSONHandler:
    def __init__(self, encoding='utf-8'):
        self.encoding = encoding

    def write_json(self, filename, data, **kwargs):
        """
        Write data to a JSON file.
        """
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        default_kwargs = {
            'ensure_ascii': False,
            'indent': 4,
            'sort_keys': True
        }
        default_kwargs.update(kwargs)

        try:
            with open(filename, 'w', encoding=self.encoding) as f:
                json.dump(data, f, **default_kwargs)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def read_json(self, filename, **kwargs):
        """
        Read a JSON file.
        """
        if not os.path.exists(filename):
            print(f"File not exist: {filename}")
            return None

        try:
            with open(filename, 'r', encoding=self.encoding) as f:
                return json.load(f, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            return None
