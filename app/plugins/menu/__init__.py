import logging
import sys
from app.commands import Command


class MenuCommand(Command):
    def description(self):
        return 'Display menu'

    def execute(self, commands_list):
        logging.info('Displayed menu')
        for command in commands_list:
                print(f"{command} - {commands_list[command].description()} command")