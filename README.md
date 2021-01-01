# datastore
A file-based key value DataStore with CRD operations.
A file-based key-value DataStore has been implemented that supports the Create, Read and Delete operations. 
The python file titled 'main.py', can be run to manipulate the local datastore.
The snapshots of various testcases can be viewed in the folder titled 'test'.

A new file 'DataStore.txt' is created the first time this program is run in the local system.
The 'Create', checks for the existence of the given key, and if it doesn't exist already, creates a key-value pair in file.
The 'Read', reads the value of a given key, if it exists.
The 'Delete', deletes a given key, if it exists.
