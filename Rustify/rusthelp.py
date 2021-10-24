# Copyright (C) 2021 RustAdmins.
# Licensed under MIT license;
# you may not use this file except in compliance with the License.
# All rights reserved.

# RustUserBot (C)

from Rustify import PATTERNS, CMD_HELP, CMD_HELP_BOT

class CmdHelp:

    FILE = ""
    ORIGINAL_FILE = ""
    FILE_AUTHOR = ""
    COMMANDS = {}
    PREFIX = PATTERNS[:1]
    WARNING = ""
    INFO = ""

    def __init__(self, file: str, file_name : str = None):
        self.FILE = file
        self.ORIGINAL_FILE = file
        self.FILE_NAME = file_name if not file_name is None else file + '.py'
        self.COMMANDS = {}
        self.FILE_AUTHOR = ""
        self.WARNING = ""
        self.INFO = ""

    def set_file_info(self, name : str, value : str):
        if name == 'name':
            self.FILE = value
        elif name == 'author':
            self.FILE_AUTHOR = value
        return self
        
    def add_command(self, command : str, params = None, usage: str = '', example = None):
        """
        Əmr əlavə edər.
        """
        
        self.COMMANDS[command] = {'command': command, 'params': params, 'usage': usage, 'example': example}
        return self
    
    def add_warning(self, warning):
        self.WARNING = warning
        return self
    
    def add_info(self, info):
        self.INFO = info
        return self

    def get_result(self):
        result = f"**📗 Fayl adı:** `{self.FILE}`\n"
        if self.INFO == '':
            if not self.WARNING == '':
                result += f"**⚠️ Diqqət:** {self.WARNING}\n\n"
        else:
            if not self.WARNING == '':
                result += f"**⚠️ Diqqət:** {self.WARNING}\n"
            result += f"**ℹ️ Məlumat:** {self.INFO}\n\n"
                     
        for command in self.COMMANDS:
            command = self.COMMANDS[command]
            if command['params'] is None:
                result += f"**🛠 Əmr:** `{PATTERNS[:1]}{command['command']}`\n"
            else:
                result += f"**🛠 Əmr:** `{PATTERNS[:1]}{command['command']} {command['params']}`\n"
                
            if command['example'] is None:
                result += f"**💬 Açıqlama:** `{command['usage']}`\n\n"
            else:
                result += f"**💬 Açıqlama:** `{command['usage']}`\n"
                result += f"**⌨️ Nümunə:** `{PATTERNS[:1]}{command['example']}`\n\n"
        return result

    def add(self):
        """
        Birbaşa CMD_HELP əlavə edər
        """
        CMD_HELP_BOT[self.FILE] = {'info': {'warning': self.WARNING, 'info': self.INFO}, 'commands': self.COMMANDS}
        CMD_HELP[self.FILE] = self.get_result()
        return True
