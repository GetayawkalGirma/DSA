# hash table or hash map is a type of data structure that maps keys to pairs
# they are implemented through the built in dictionary data types
# dictionaries can be created using two ways
#FIRST : USING CURLY BRACES {}
mydict={'dave':'001','dani':'002','joe':'003'}
print(mydict)
type(mydict)

# SECOND : BY USING THE DICT FUNCTION dict()

# TO CREATE EMPTY DICTIONARY

empty_dict=dict()
print(empty_dict)

# TO ADD VALUES
newdict=dict(dave='01',dani='02',joe='03')
print(newdict)
type(newdict)

# NESTED DICTIONARIES
# ITS A DICTIONARY WITH IN A DICTIONARY
studentdetails={'studentname':{'Getayawkal':{'id':'0316/12','department':'EME','year':'5th'},
         'Gedion':{'id':'0311/12','department':'EME','year':'5th'}}}
print(studentdetails)

# PERFORMING OPERATION ON HASH TABLES

# ACCESING ITMES

print('0')
print(mydict['dave'])

print('1')
print(mydict.keys())

print("2")
print(mydict.values())

print('3')
print(mydict.get('joe'))

# USING FOR LOOP TO FIND

print("for keys in dict print the key ")

for x in mydict:
    print(x)

print('same but to find values ')

for x in mydict.values():
    print(x)

print('to find both key and values USE mydict.items()')

for x,y in mydict.items():
    print(x,y)

# UPDATING THE VALUES

mydict['dave']='005'
mydict['ajrew']='006'
print(mydict)

# DELETING ITEMS

mydict.pop('dani')

mydict.popitem()

print(mydict)

del mydict['dave']

print(mydict)


# CONVERTING DICTIONARY IN TO A DATA FRAME

import pandas as pd
df= pd.DataFrame(studentdetails['studentname'])
print(df)