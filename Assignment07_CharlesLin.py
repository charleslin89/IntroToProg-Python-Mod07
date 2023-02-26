# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Show understanding of Pickling and Error Handling
# 1. Initialize and seed a dictionary with 2 customers
# 2. Write to a binary file
# 3. Read content from the binary file
# 4. Write to a text file Observe how data looks on binary and text files
# 5. Turn reading binary file into a function
# 6. Add try/except to read text file
# 7. Place try/except in the read function to treat scenario when text file is not found
# 8. Show data to user and ask if a user wants to write to a binary or text file
# 9. Write data to what the user selected
# ChangeLog: Charles Lin 2023-02-23 Outlining the steps
# CLin, 2023-02-22 Created file
# ---------------------------------------------------------------------------- #

# Declare variables
binary_file_name = "CustomerData.dat"
text_file_name = "CustomerData.txt"
filePath = "CustomerDat.txt"
lstTable=[]
list_of_rows=[]
strChoice = ""


# Step 1 - initializing customer data to be stored in dictionary
# -------------------------------------------------------------------------
dicRow1 = {"ID": 1, "Name": "Mary Johnson", "Email":"MJohnsohn@msn.com"}
dicRow2 = {'ID': 2, "Name": "Susan Jones", "Email":"SJones@hotmail.com"}
lstCustomer = [dicRow1, dicRow2]

# Step 2 - Write to a binary file with pickle.dump
# -------------------------------------------------------------------------
import pickle  # This imports code from another code file

objFile = open(binary_file_name, "wb")
pickle.dump(lstCustomer, objFile)
objFile.close()
print("Binary file has been written.")
print("--------------------------------------------------------------")

# Step 3 - Read and display data from binary file with pickle.load
# -------------------------------------------------------------------------
objFile = open(binary_file_name, "rb")
objFileData = pickle.load(objFile)
for objRow in objFileData:
    print(str(objRow["ID"]) + '|' + objRow["Name"] + '|' + objRow['Email'])
objFile.close()
print("--------------------------------------------------------------")

# Step 4 - Observe file size difference if written to a text file
# -------------------------------------------------------------------------
objFile = open(text_file_name, "w")
for objRow in lstCustomer:
    objFile.write(str(objRow["ID"]) + ',' + str(objRow["Name"]) + ',' + str(objRow["Email"]) + '\n')
objFile.close()
print()
print("The dictionary is also written to a text file to observe sizes.")
print("--------------------------------------------------------------")
print()

# Step 5 - Turn reading binary file into a function
# -------------------------------------------------------------------------
def read_data_from_file(file_name):
    """ Reads data from a binary file into a list of dictionary rows

    :return: (list) of dictionary rows
    """
    import pickle

    objFile = open(file_name, "rb")
    objFileData = pickle.load(objFile)
    objFile.close()

# Step 6 - Add try/except to read text file
# -------------------------------------------------------------------------
try:
    objFile = open(filePath, "r")
    for row in objFile:
        ID, Name, Email = row.split(",")
        row = {"ID": ID.strip(), "Name": Name.strip(), "Email": Email.strip()}
        list_of_rows.append(row)
    objFile.close()
    print("Try Except Example of reading a text file, and the file is available:")
    print("--------------------------------------------------------------")
    for objRow in list_of_rows:
        print(str(objRow["ID"]) + '|' + objRow["Name"] + '|' + objRow['Email'])
    print("--------------------------------------------------------------")
except FileNotFoundError as e:
    print("Try Except Example when the file it tries to read is not available.")
    print("Change 'filePath' Variable on Line 20 to 'CustomerData.txt' to proceed.")
    print("--------------------------------------------------------------")
    print("The Built-In Python error Info shows - ")
    print(e)
    print("No data would return.")
    print()

# Step 7. Place try/except in the read function to treat scenario when text file is not found
# -------------------------------------------------------------------------
def read_data_fromfile():
    """Reads data from text file into a list of dictionary rows

    :return: (list) of dictionary rows
    """
    list_of_rows.clear()
    try:
        objFile = open(filePath, "r")
        for row in objFile:
            ID, Name, Email = row.split(",")
            row = {"ID": ID.strip(), "Name": Name.strip(), "Email": Email.strip()}
            list_of_rows.append(row)
        objFile.close()
        return list_of_rows
    except FileNotFoundError as e:
        print("The file it tries to read is not available.")
        print(e)
        print(type(e))
        print()

# 8. Show data to user and ask if a user wants to write to a binary or text file
# -------------------------------------------------------------------------
print()
print("Read the result from the function to write records below to a binary or text file decideed by user:")
print("--------------------------------------------------------------")

while(True):
    if read_data_fromfile() is not None:  # Check if a value is None or not from function before iterating over it.
        print("This is the list of customers")
        print("--------------------------------------------------------------")
        for objRow in read_data_fromfile():
            print(str(objRow["ID"]) + '|' + objRow["Name"] + '|' + objRow['Email'])
        print("--------------------------------------------------------------")

        strChoice = input("Choose [b] to write to a binary file or [t] to write to a text file, or [Exit] to finish: ")

        if (strChoice.lower() == 'exit'): break # Exits out of while loop

        elif (strChoice.lower()) == 'b':
            objFile = open("CustomerDataFromFunction.dat", "wb")
            pickle.dump(list_of_rows, objFile)
            objFile.close()
            print('Data written to a binary file.')
            print()
        elif (strChoice.lower() == 't'):
            objFile = open("CustomerDataFromFunction.txt", "w")
            for objRow in list_of_rows:
                objFile.write(str(objRow["ID"]) + ',' + str(objRow["Name"]) + ',' + str(objRow["Email"]) + '\n')
                # objFile.write(str(objRow["ID"]) + ',' + str(objRow["Name"]) + ',' + str(objRow["Email"]) + '\n')
            print('Data written to a text file.')
            print()
        else:
            print('Please choose either B or T!')
    else:
        print("Cannot read any data to write from.")
        print("Change 'filePath' Variable on Line 20 to 'CustomerData.txt' to proceed.")
    break
    continue

input('Press Enter to Exit')





