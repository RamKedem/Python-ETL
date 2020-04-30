1. The way I've implemented the credentials via env variables is secured enough ?
   Are you recommending any other way ?

2. Logging, this is the first time I'm using the logging module :)
2.1 Is the logging_config.conf designed well enough ?
2.2 Is it a good practice to use .conf files ?
    I know there are several other options such as yaml/json
    If not, what is your recommendation ?
2.3 In the core etl code - have I used the logging well enough ?
    - Setting the logger
    - Extensively logging each phase

3. Validating sys.argv
   In daily_load.py - since the user is allowed to insert 0 or 1 argument,
   I've implement series of If statements and functions to allow it.
   Are they designed well enough ?

4. Designing the readme.md file
    Not experienced enough with desiging / writing these kind of files,
    whould love to hear feedback / feedback on how I should write those files

5. etl folder, __init__.py file.
   As far as I understand this is not nessesary from Python 3.3 onwards ?
   https://stackoverflow.com/questions/448271/what-is-init-py-for

6. In the load.py you wrote the following comment :
   You can capitalize acronyms in class names / variables
   according to pep08, variable names should always be at lower caps ? Am I wrong ?

7. Using multiple return statements, according one of your comments:

Say I have the following logic inside a function :

if condition_1:
    x = 1
elif condition_2:
    x = 2
else:
    x = 3
return x

would it be better if I just return x in each condition :

if condition_1:
    return 1
elif condition_2:
    return 2
...
 
8. In extract.py you wrote the following code. It failed on execution

    def get_csv_data(self, date, csv_name):
        return _get_core(self, date, csv_name, "excel")

    def get_excel_data(self, date, excel_name):
        return _get_core(self, date, excel_name, "excel")

    I change it to the following. Am I missing something ?

        def get_csv_data(self, date, csv_name):
            return self._get_core(date, csv_name, "csv")

        def get_excel_data(self, date, excel_name):
            return self._get_core(date, excel_name, "excel")
