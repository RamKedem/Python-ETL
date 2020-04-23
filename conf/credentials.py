from os import getenv

sql_server_target = {
    'server': getenv("MSSQL_SERVER_NAME"),
    'instance': getenv("MSSQL_INSTANCE"),
    'database': getenv("MSSQL_DATABASE"),
    'Trusted_Connection': 'yes',
    'user': getenv("MSSQL_USERNAME"),
    'password': getenv("MSSQL_PASSWORD"),
    'driver': 'ODBC Driver 17 for SQL Server',
  }
