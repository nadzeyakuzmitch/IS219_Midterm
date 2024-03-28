import logging
import os
from app.commands import Command
import pandas as pd


class HistoryCommand(Command):
    def description(self):
        return 'History menu'

    def execute(self, commands_list):

        try:
            data_dir = './history'
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
                logging.info(f"The directory '{data_dir}' is created")

            elif not os.access(data_dir, os.W_OK):
                logging.error(f"The directory '{data_dir}' is not writable.")
                return
        except:
            logging.error(f"Error initializing history feature")


        print("\n---------------\nHistory menu (type 'cancel' for main menu)\n")
        print("show - Show calculations history\nclear - Clear current calculations history\nload - Load calculations history from storage\nsave - Save calculations history to storage\ndelete - Clear calculations history storage\n")
        isWorking = True
        while isWorking:  #REPL Read, Evaluate, Print, Loop
            input_command = input("HISTORY MENU >>> ").strip()
            if input_command == 'cancel':
                isWorking = False
            try:
                print(f"{input_command}")
                getattr(self, input_command)()
                isWorking = False
            except:
                print(f"\n---------------\nNo such command: {input_command}\n---------------\n")
    
    def show(self):
        return
    
    def clear(self):
        return
    
    def load(self):
        return
    
    def save(self):
        return
    
    def delete(self):
        return
