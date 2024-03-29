import os
import pkgutil
import importlib
import sys
from app.commands import CommandHandler, Command
from dotenv import load_dotenv
import logging
import logging.config

class App:
    def __init__(self): # Constructor
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION') # Reading ENV variable for enviroment type
        logging.info(f'Environment: {self.get_environment_variable()}')
        self.command_handler = CommandHandler()
        self.local_history = [] # Initializing apps history

    def configure_logging(self): # Basic logging configuration
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self): # Helper funciton to load ENV variables
        settings = {key: value for key, value in os.environ.items()}
        logging.info(f'Environment variables loaded.')
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'): # Helper function to actually retrieve ENV variables
        return self.settings.get(env_var, None)

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
                            logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore
    def start(self):
        # Register commands here
        self.load_plugins()
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(f'Type operation command or type `menu` for available commands (type `exit` to exit):\n{self.get_environment_variable()} >>> ').strip(), self.local_history) # Passing history storage down to commands



