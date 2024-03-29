import logging
import sys
from app.commands import Command


class MenuCommand(Command):
    def description(self):
        return 'Display menu' # Simple factory pattern: initializing command description with the class initialization

    def execute(self, commands_list, local_history):
        logging.info('Displayed menu')
        print(f'\n---------------\nAvailable commands:\n')
        for command in commands_list: # Displaying registered commands from the list passed down from parent class
                print(f"{command} - {commands_list[command].description()} command")
        print(f'---------------\n')