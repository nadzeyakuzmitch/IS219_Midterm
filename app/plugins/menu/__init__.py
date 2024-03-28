import logging
import sys
from app.commands import Command


class MenuCommand(Command):
    def description(self):
        return 'Display menu'

    def execute(self, commands_list, local_history):
        logging.info('Displayed menu')
        print(f'\n---------------\nAvailable commands:\n')
        for command in commands_list:
                print(f"{command} - {commands_list[command].description()} command")
        print(f'---------------\n')