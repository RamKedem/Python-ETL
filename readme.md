# Python ETL 
## About
Python ETL program, written in `python 3`
## Main Features
- Supports CSV and Excel as data sources
- Supports MSSQL Server as target
- Supports daily and range loads

## Install and Setup
- Clone the repo
- Create a virtual env
- Install the `requirements.txt` dependencies

## Usage
The program supports the following procedures : 
- `daily_load.py` executes a daily ETL process. 
 - Can be executed without any arguments, defaults to the current date
 - Can be executed with specific date
 
 ```
 daily_load.py
 daily_load.py 23_01_2020
 ```
 
- `range_load.py` - supports ETL process for a given range of dates
 
 ```
 range_load.py  23_01_2020 28_01_2020
 ```

Please note:
1. The dates must be written according the following format `DD_MM_YYYY` 

## Structure 

```
│   daily_load.py
│   range_load.py
│   requirements.txt


├───conf
│      credentials.py				# Target database credential file 
│      logging_config.conf			# Logging configuration
│      sources_config.json			# Source files configuration file
│   


├───data					# Data Folder - Structured as:
						# DATE/TYPE/SOURCE_NAME/SOURCE_FILES

├───etl
│   │   engine.py				# Calling the ETL modules
│   │   extract.py				# Extract portion
│   │   helpers.py				# Helper functions, used by the Load portion
│   │   load.py					# Load portion
│   │   transform.py				#Transform portion
│   │   __init__.py


├───logs
│       logfile.log				# Log File

```

