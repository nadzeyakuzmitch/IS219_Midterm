from abc import ABC, abstractmethod

class Command(ABC):
    """Added description property to use it in menu functionality"""
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
        """Try Catch block tohandle unknown commands (LBYL)"""
        try:
            print(f"{command_name}")
            """Main central commands execution code, passes history down for modification"""
            self.commands[command_name].execute(self.commands, local_history)
        except KeyError:
            print(f"\n---------------\nNo such command: {command_name}\n---------------\n")

