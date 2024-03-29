# Project: Midterm | Advanced Calculator with History and Local Storage

## Setup instructions 

1. Clone repository and install requirements

```bash
git clone git@github.com:kaw393939/git_python_testing_setup_homework.git
cd git_python_testing_setup_homework
source venv/bin/activate
pip3 install -r requirements.txt
```

2. To run the app run the following

```bash
python3 ./main.py
```

3. To test the app run the following

```bash
pytest --pylint --cov
```

## App Manual

1. Start the app
2. Type commands that you need to run, the list is following:
```
add - Addition operation command
divide - Division operation command
exit - App exit command
history - History menu command
menu - Display menu command
multiply - Multiplication operation command
subtract - Subtraction operation command
```
3. Follow informational prompts after running the command
4. Type the following to exit application:
```
exit
```

## Usage of the design patterns

1. REPL: Read-Eval-Print-Loop pattern is being used for the main application functionality. With the help of the while loop we can continuosly run multiple commands untill user trigger key word to stop the application. I use that method for the main menu and additional REPL instance for calculator operations and history functionalities.

2. LBYL: Look-Before-You-Leap pattern is being used for the scenarios where I need to check if the directory for manipulating history data can be used; otherwise I restrict functionality based on that.

3. EAFP: Easier-to-Ask-for-Forgiveness-than-Permission patter is being used in multiple places - trying to get away with launching unknown commands, trying ot delete/load non-exhistend files, trying to perform math operations which are forbidden.

4. Facade: pattern which created "facades" for the complited code to simplify the end use. I use that patter in the history functionality to generate string to display or create data entries for the Pandas DataFrame.

5. Factory Method: I somewhat use that method to initialize every command module with the descirption which is used for an automatic display of the available commands with the descriptions.

## Usage of ENV variables

I use a single enviromental variable called 'envoroment' which is used to display a proper info message while running the program.

## Ussage of logging

Logging is used all across the app. I use it to show info messages about executed commands, info messages about changes to the history, error messages when critical exceptions are caught.