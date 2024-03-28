import logging
import os
import sys
from app.commands import Command
import pandas as pd


class HistoryCommand(Command):
    def description(self):
        return 'History menu'

    def execute(self, commands_list, local_history):
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
        while isWorking:  #REPL Read, Evaluate, Print, Loop
            input_command = input("HISTORY MENU >>> ").strip()
            if input_command == 'main':
                print('')
                isWorking = False
                return

            if input_command == 'exit':
                logging.info('Exiting app')
                sys.exit("Exiting...")

            print(f"{input_command}")
            getattr(self, input_command)(local_history, data_dir)
            # try:
            # except:
            #     print(f"\n---------------\nNo such command: {input_command}\n---------------\n")
    
    def show(self, local_history, data_dir):
        if len(local_history) == 0:
            print("\n---------------\nLocal history is empty\n---------------\n")
            return
        print("\n---------------\nLocal history:")
        for record in local_history:
            print(self.record_string(record))
        print("---------------\n")
        return
    
    def clear(self, local_history, data_dir):
        local_history.clear()
        print("\n---------------\nLocal history has been succesfully cleared\n---------------\n")
        return
    
    def load(self, local_history, data_dir):
        read_history = None
        try:
            local_history.clear()
            csv_file_path = os.path.join(data_dir, 'history.csv')
            read_history = pd.read_csv(csv_file_path)
        except:
            print("\n---------------\nNo stored history file available\n---------------\n")
            return
        
        for index, row in read_history.iterrows():
            historyRecord = {
                'index': index,
                'operation': row['Operation'],
                'arg_a': row['Argument A'],
                'arg_b': row['Argument B'],
                'result': row['Result']
            }
            local_history.append(historyRecord)

        print("\n---------------\nStored history has been succesfully loaded\n---------------")
        self.show(local_history, data_dir)
        return
    
    def save(self, local_history, data_dir):
        df = pd.DataFrame([self.record_to_dict(item) for item in local_history])
        csv_file_path = os.path.join(data_dir, 'history.csv')
        df.to_csv(csv_file_path, index=False)
        print("\n---------------\nLocal history data has been succesfully stored\n---------------\n")
        return
    
    def delete(self, local_history, data_dir):
        csv_file_path = os.path.join(data_dir, 'history.csv')
        os.remove(csv_file_path)
        print("\n---------------\nStored history data has been succesfully removed\n---------------\n")
        return

    def record_string(self, record):
        return f"#{record['index']} | Operation: {record['operation']}; A: {record['arg_a']}, B: {record['arg_b']}; Result - {record['result']}"
    
    def record_to_dict(self, record):
        return {'Operation':record['operation'], 'Argument A': record['arg_a'], 'Argument B': record['arg_b'], 'Result': record['result']}