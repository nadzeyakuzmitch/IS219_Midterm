import logging
from decimal import Decimal
from app.commands import Command


class SubtractCommand(Command):
    def description(self):
        return 'Subtraction operation'

    def execute(self, commands_list, local_history):
        print("\n---------------\nSubtraction operation (type 'stop' for main menu)\n")
        isWorking = True
        while isWorking:  #REPL Read, Evaluate, Print, Loop
            a = input("Enter A:\n>>> ").strip()
            if a == 'stop':
                print("Operation cancelled\n---------------\n")
                isWorking = False
                break
            b = input("Enter B:\n>>> ").strip()
            if a == 'stop':
                print("Operation cancelled\n---------------\n")
                isWorking = False
                break
            try:
                result = subtract(Decimal(a), Decimal(b))
                print(f"Result is:\na - b = {a} - {b} = {result}\n---------------\n")
                logging.info(f'Operation result: {result}')
                isWorking = False
                add_to_history(a, b, result, local_history)
            except Exception as e: # Catch-all for unexpected errors
                print(f"An error occurred: {e}\n---------------\n")
                logging.error(f"Error while executing command: {e}")
                isWorking = False

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def add_to_history(a, b, result, local_history):
    logging.info(f'Added to history: {a} {b} {result}')
    local_history.append({
        'index': len(local_history),
        'operation': 'subtract',
        'arg_a': a,
        'arg_b': b,
        'result': result
    })
    return
