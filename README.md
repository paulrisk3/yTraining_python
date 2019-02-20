# yTraining_python
Flask server to parse CSV files and return JSON

## Configuring the App
First, please place an updated CSV containing yTraining records into the "data" folder. This CSV should be two columns. The first column should contain the net ID of a user (this app expects all net IDs to be in all caps). The second column should contain the full name of a training that the user has completed.

Second, please place the name of this file into the "records_file" variable, found on line 13 of app.py.

## Running the App
Run by opening a terminal, navigating to the primary folder (yTraining_python), and running "python app.py". 
