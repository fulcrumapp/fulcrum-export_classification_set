# fulcrum-export_classification_set
This tool can be used to export classification sets to a csv file. 


A library for getting a csv file of classification sets produced in Fulcrum.

# Option 1 (from API)

## Requirements
Requires python installed, [Fulcrum Python API wrapper](https://github.com/fulcrumapp/fulcrum-python) installed, Fulcrum API token, and the ID of the classification set.    

classification set ID can be obtained from the web app.  When the classification set is open for an edit within [web.fulcrumapp.com](https://web.fulcrumapp.com/) you can get the classification set ID from the address bar between the text that reads /classification_sets and /edit

## Usage
Run the script from terminal with `python classification-set-to-csv-with-API.py -t {token} -cs {classification_set_id}`

# Option 2 (from file)

## Requirements
Requires python installed and .classes files from classification set. 

.classes file can be produced from the web app.  When the classification set is open for an edit within [web.fulcrumapp.com](https://web.fulcrumapp.com/) you can change `/edit` in the address bar of your web browser to `/export` to produce the .classes file. 

## Usage
In the python script, change the name of the file to match the file that you have downloaded from Fulcrum.

The python script and classes file will need to be in the same folder.

Run the script from terminal with `python classification.py --input 'file-name.classes'`
