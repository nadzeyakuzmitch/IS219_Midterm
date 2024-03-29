import logging
import os
import sys
from app.commands import Command
import pandas as pd


class HistoryCommand(Command):
    def description(self):
        return 'History menu' # Simple factory pattern: initializing command description with the class initialization

    def execute(self, commands_list, local_history):
        # Checking if we have power to write history directory - unable to use history feature otherwise
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

        print("\n---------------\nHistory menu (type 'main' for main menu, 'exit' to exit)\n")
        print("show - Show calculations history\nclear - Clear current calculations history\nload - Load calculations history from storage\nsave - Save calculations history to storage\ndelete - Clear calculations history storage\n---------------\n")
        isWorking = True
        while isWorking: # REPL for history menu
            input_command = input("HISTORY MENU >>> ").strip()
            if input_command == 'main': # Main command returns to the main menu
                print('')
                isWorking = False
                return

            if input_command == 'exit': # Exit will exit the app
                logging.info('Exiting app')
                sys.exit("Exiting...")

            print(f"{input_command}")
            logging.info(f"Running history command: {input_command}")
            try:
                getattr(self, input_command)(local_history, data_dir) # Based on the input trying to launch local command
            except:
                logging.error(f"Unknown history command: {input_command}") # If command is not found then showing info about available commands again
                print(f"\n---------------\nNo such command: {input_command}\n---------------")
                print("\n---------------\nHistory menu (type 'main' for main menu, 'exit' to exit)\n")
                print("show - Show calculations history\nclear - Clear current calculations history\nload - Load calculations history from storage\nsave - Save calculations history to storage\ndelete - Clear calculations history storage\n---------------\n")
    
    """Displaying local history"""
    def show(self, local_history, data_dir):
        if len(local_history) == 0:
            print("\n---------------\nLocal history is empty\n---------------\n")
            return
        print("\n---------------\nLocal history:")
        for record in local_history:
            print(self.record_string(record))
        print("---------------\n")
        logging.info(f"Displayed history")
        return
    
    """Clearing local history"""
    def clear(self, local_history, data_dir):
        local_history.clear()
        print("\n---------------\nLocal history has been succesfully cleared\n---------------\n")
        logging.info(f"Cleared local history")
        return
    
    """Loading stored history into local"""
    def load(self, local_history, data_dir):
        read_history = None
        try:
            local_history.clear()
            csv_file_path = os.path.join(data_dir, 'history.csv') # Reading csv file
            read_history = pd.read_csv(csv_file_path) # Parsing CSV file with the help of Pandas
        except:
            print("\n---------------\nNo stored history file available\n---------------\n")
            logging.info(f"No stored history found")
            return
        
        for index, row in read_history.iterrows(): # Converting parsed data into usable data array
            historyRecord = {
                'index': index,
                'operation': row['Operation'],
                'arg_a': row['Argument A'],
                'arg_b': row['Argument B'],
                'result': row['Result']
            }
            local_history.append(historyRecord) # Saving to the local history

        print("\n---------------\nStored history has been succesfully loaded\n---------------")
        self.show(local_history, data_dir) # Displaying loaded history
        logging.info(f"Stored history loaded")
        return
    
    def save(self, local_history, data_dir):
        try:
            df = pd.DataFrame([self.record_to_dict(item) for item in local_history]) # Converting local array to the format necessary for CSV
            csv_file_path = os.path.join(data_dir, 'history.csv')
            df.to_csv(csv_file_path, index=False) # Saving data to CSV using the file path
            print("\n---------------\nLocal history data has been succesfully stored\n---------------\n")
            logging.info(f"Local history saved")
        except:
            print("\n---------------\nThere was a problem during saving of the local data\n---------------\n")
            logging.error(f"Error saving local history")
        return
    
    def delete(self, local_history, data_dir):
        try:
            csv_file_path = os.path.join(data_dir, 'history.csv')
            os.remove(csv_file_path) # Trying to remove stored file
            print("\n---------------\nStored history data has been succesfully removed\n---------------\n")
            logging.info(f"Stored history deleted")
        except:
            print("\n---------------\nThere was a problem during deletion of the stored data\n---------------\n")
            logging.info(f"Error deleting stored history")
        return

    def record_string(self, record): # Facade Pattern: funciton to convert history record into user friendly string
        return f"#{record['index']} | Operation: {record['operation']}; A: {record['arg_a']}, B: {record['arg_b']}; Result - {record['result']}"
    
    def record_to_dict(self, record): # Facade Pattern: function to convert record to the usable element for Pandas
        return {'Operation': record['operation'], 'Argument A': record['arg_a'], 'Argument B': record['arg_b'], 'Result': record['result']}