**Name:** Charles Lin

**Date:** February 22, 2023

**Course:** IT FDN 110 A

**GitHubURL:** [https://github.com/charleslin89/IntroToProg-Python-Mod07](https://github.com/charleslin89/IntroToProg-Python-Mod07)

# Assignment 07 Files and Exceptions

## Introduction

I learned about working with text and binary files, getting to the specific row, ways to build error exception codes, using pickle function to read binary file, and building GitHub web page.

## Reading and Writing Text Files

We can open(), write(), and close() text files. After we open a file, we can also pick out specific rows to put in a list by looping through rows and looking up the particular value match. When writing, we have the option to append to existing rows or overwrite the whole file. Codes relating to file treatments can be grouped into a function.

In addition to plain text files, there are binary files that are obscured but not encrypted. The content is harder to read in a binary file. In Python we can dump the content and use pickle.load method to read the content.

## Pickling Feature
Pickling is used to store python objects. This means things like lists, dictionaries, class objects, and more. If we have a large dataset, and we're loading that massive data set into memory every time we run the program, it makes a lot of sense to pickle it, and then load that instead, because it will be far faster than a csv text file.

[Python Pickle Module](https://realpython.com/python-pickle-module/)
The process of serialization to send complex object hierarchies over a network or save the internal state of your objects to a database. Serialization converts a data structure into a linear form that can be stored or transmitted over a network. Python serializes objects in a binary format, which means the result is not human readable. Though it’s faster, and it works with many more Python types right out of the box. Python team use terms pickling and unpickling to refer to serializing and deserializing. We can dump() or load() data in pickle module.

[Python Numerical Methods’ Pickle Files](https://pythonnumericalmethods.berkeley.edu/notebooks/chapter11.03-Pickle-Files.html)
The term “pickle” comes from saving dictionaries, lists, etc to share with others, like pickling vegetables. The link was published a few years back, but I find the pickle concept and examples easy to follow.

## Error Handling
Try-Except lets us communicate error messages that are more meaningful. We can customize the error message by 

[LinkedIn Learning Script 5: Error Handling](https://www.linkedin.com/learning/search?keywords=python%20error%20handling&u=2091572) **LinkedIn Learning License Required**
Notes: Building in Try-Except gives us the option to let other portions of the job to run, instead of failing all together. 

[All About Exceptions](https://www.learnpython.dev/03-intermediate-python/40-exceptions/10-all-about-exceptions/)
Notes: The navigation of the webpage is curious, but the content layout is similar to Professor Root’s lecture material.

## Assignment with Pickling and Structured Error Handling 
I want my script to do the following:

1. Initialize and seed a dictionary with 2 customers
2. Write to a binary file
3. Read content from the binary file
4. Write to a text file Observe how data looks on binary and text files
5. Turn reading binary file into a function
6. Add try/except to read text file
7. Place try/except in the read function to treat scenario when text file is not found
8. Show data to user and ask if a user wants to write to a binary or text file
9. Write data to what the user selected

On Pickling and Structured Error Handling (Try/Except)

### Pickling
The code writes 2 rows of customer data from a list of rows to a binary file, then deserializes and reads the binary file’s content to a dictionary.
```
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
```
Listing 1 Try/Except to give meaningful message

![Figure 1](./assets/Figure1.png)

Figure 1 The result of List 1 


![Listing 2](./assets/Listing2.png)

Listing 2 Binary file opened in TextEdit reader 

I wondered if the size of binary file helps with faster processing speed. I wrote the list from Listing 1 to a txt file to observe the size difference. Txt file was smaller than binary file. So I think the faster processing comes from an easier processing mechanism, and not from the file size. 

```
objFile = open(text_file_name, "w")
for objRow in lstCustomer:
    objFile.write(str(objRow["ID"]) + ',' + str(objRow["Name"]) + ',' + str(objRow["Email"]) + '\n')
objFile.close()
print()
print("The dictionary is also written to a text file to observe sizes.")
print("--------------------------------------------------------------")
print()
```

Listing 3 Write to a txt file 

![Figure 2](./assets/Figure2.png)

Figure 2 Txt file from Listing 3 

![Figure 3](./assets/Figure3.png)

Figure 3 Size comparison between text and binary files

### Try/Except
When I read a file, if a file doesn’t exist and I didn’t include any try/except, I would get a FileNotFoundError, and the job stops. In this example, I missed the last “a” in CustomerData. I have “CustomerDat.txt” in the script, and the job stops there.

![Listing 4](./assets/Listing4.png)

Listing 4 Reading a file with wrong file name that doesn’t exist

![Figure 4](./assets/Figure4.png)

Figure 4 Error message with no try/except

If I include a try/except, I can customize the error message and the job can continue.

![Listing 5](./assets/Listing5.png)

Listing 5 With try/except with built-in FileNotFoundError

![Figure 5](./assets/Figure5.png)

Figure 5 Result from Listing 5 that shows the error and the job continues to the next step

I intentionally set variable filePath to be “CustomerDat.txt” to illustrate the exception error. I customized the error to show Python’s Built-in exception and to communicate nothing will show.

![Listing 6](./assets/Listing6.png)

Listing 6 Variable “filePath” that points to a file that doesn’t exist so cannot be read from

![Figure 6](./assets/Figure6.png)

Figure 6 Built-in exception object and customized message when “filePath” from Listing 6 cannot be found

The output in Terminal when the file cannot be found (variable filePath = “CustomerDat.txt”)

![Listing 7](./assets/Listing7.png)

Listing 7 When file is not found, message shows built-in exception and communicates the file is not available

When variable filePath is set to “CustomerData.txt”, then the data can be read, and this is the output in Terminal when the user chooses to write to a binary file. The user can also choose to write to a text file.

![Listing 8](./assets/Listing8.png)

Listing 8 When the file is available, it shows the records that will be written and tells the user the it is writing to a binary file.

The selected file type then is written in the working folder. 

![Figure 8](./assets/Figure8.png)

Figure 8 Binary file written by Listing 8

![Figure 9](./assets/Figure9.png)

Figure 9 Text file written by Listing 8

## Summary
When the assignment request is very high-level, I need to think of a code design that is feasible with what I know, and fulfills the requirements.  I have a good sense of error handling (try/except), and I’m becoming familiar with publishing GitHub’s page.










