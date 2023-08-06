import json, os
from pathlib import Path

file = r"C:\Users\kylea\github\kypy-module\dictionary.json"

with open(file, "r") as ofile:
    #contents = ofile.read() # string
    contents = json.load(ofile) # list

contents_length = len(contents) # 1 
# not sure if all responses are going to just be one
if contents_length > 1:
    print("Check: response list greater than 1.")
else:
    pass

contents_dict = contents[0]
# key: meta, hwi, fl, ins, def, quotes, et, date, shortdef

meta = contents_dict["meta"] # dict
# keys: id, uuid, sort, src, section, stems, offensive
hwi = contents_dict["hwi"] # dict
# keys: hw, prs
fl = contents_dict["fl"] # string
# noun
ins = contents_dict["ins"] # list

deff = contents_dict["def"] # list, length 1, containing dictinoary

quotes = contents_dict["quotes"] # list, length 2, containing dict

et = contents_dict["et"] # list, length 1

date = contents_dict["date"] # string

shortdef = contents_dict["shortdef"] # list, length 3, containing strings


