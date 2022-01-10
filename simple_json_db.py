import json
from json.decoder import JSONDecodeError
from os import read
from dataclasses import dataclass

@dataclass
class SJDStatusCodes:
    SUCCESS = 0
    FILE_NOT_INITIALIZED = 1
    FILE_NOT_FORMATTED = 2

class SimpleJSONDatabase:
    def __init__(self, file: str, form: set) -> None:
        self.file = file
        self.form = form

        self._handle_status_code(self._is_formed())
    
    def _init_db(self) -> None:
        open(self.file, "w").close()

    def _format_db(self) -> None:
        with open(self.file, "w+") as f:
            _json = {k:None for k in self.form}
            json.dump(_json, f)

    def _handle_status_code(self, code: SJDStatusCodes) -> None:
        if(code == SJDStatusCodes.SUCCESS):
            return
        elif(code == SJDStatusCodes.FILE_NOT_INITIALIZED):
            self._init_db()
        elif(code == SJDStatusCodes.FILE_NOT_FORMATTED):
            self._format_db()
        
        self._handle_status_code(self._is_formed())
    
    def _is_formed(self) -> SJDStatusCodes:
        try:
            open(self.file, "r").close()
        except FileNotFoundError:
            return SJDStatusCodes.FILE_NOT_INITIALIZED
        try:
            with open(self.file, 'r') as f:
                _json = json.load(f)
                for key in list(self.form.keys()):
                    if(key not in list(_json.keys())):
                        return SJDStatusCodes.FILE_NOT_FORMATTED
        except JSONDecodeError:
            return SJDStatusCodes.FILE_NOT_FORMATTED
        return SJDStatusCodes.SUCCESS


