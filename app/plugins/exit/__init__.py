import logging
import sys
from app.commands import Command


class ExitCommand(Command):
    def description(self):
        return 'App exit'

    def execute(self, commands_list):
        logging.info('Exiting app')
        sys.exit("Exiting...")