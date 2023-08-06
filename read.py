import json, os
from pathlib import Path
import pandas as pd

file = r"C:\Users\kylea\github\kypy-module\dictionary.json"

with open(file, "r") as ofile:
    #contents = ofile.read() # string
    contents = json.load(ofile) # list

def checkLen(thing):
    '''check length of something, alert if longer than one'''
    if len(thing) > 1:
        print("Check-- list greater than 1.")
    else:
        pass
    return len(thing)

howlong = checkLen(contents)

# generator json test
def tester(structured_data):
    initial_check = checkLen(structured_data)
    for part in structured_data:
        yield part

def nexter(gen_object):
    '''accepts generator function, calls next'''
    print(next(gen_object))
    return gen_object

contents_dict = contents[0]

def first(content_dict):
    for x in content_dict:
        yield x

dataframe_file = pd.read_json("dictionary.json")
print(dataframe_file)