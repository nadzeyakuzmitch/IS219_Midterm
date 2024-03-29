import logging
import sys
from app.commands import Command


class ExitCommand(Command):
    def description(self): # Simple factory pattern: initializing command description with the class initialization
        return 'App exit'

    def execute(self, commands_list, local_history):
        logging.info('Exiting app')
        sys.exit("Exiting...")