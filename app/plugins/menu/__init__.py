import logging
import sys
from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        logging.info('Displayed menu')
        print(f'\n---------------\nAvailable commands:\n\nadd - Addition operation\nsubtract - Subtraction operation\nmultiply - Multiplication operation\ndivide - Division operation\n\nexit - Exit application\n---------------\n')