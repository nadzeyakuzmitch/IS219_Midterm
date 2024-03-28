from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def execute(self, commands_list, local_history):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str, local_history):
        """ Look before you leap (LBYL) - Use when its less likely to work
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")
        """
        """Easier to ask for forgiveness than permission (EAFP) - Use when its going to most likely work"""
        self.commands[command_name].execute(self.commands, local_history)
        # try:
        #     print(f"{command_name}")
        #     self.commands[command_name].execute(self.commands, local_history)
        # except KeyError:
        #     print(f"\n---------------\nNo such command: {command_name}\n---------------\n")

