import jmespath, json

file = r"C:\Users\kylea\github\kypy-module\dictionary.json"

with open(file, "r") as ofile:
    data = ofile.read()

#search = jmespath.search("meta", data)
#print(search)

with open(file, "r") as ofile:
    jsondata = json.load(ofile) # list

def checkLen(boop):
    if len(boop) > 1:
        print("length greater than 1. check.")
    else:
        pass

checkLen(jsondata)

x = len(jsondata) - 1
corrected = jsondata[x]

def yielder(thing):
    for piece in thing:
        yield piece

def nexter(thang):
    print(next(thang))
    return next(thang)

def ranger(thong):
    print(len(thong))
    return len(thong)

part = yielder(corrected)

for key in corrected:
    print(key, type(key), len(key))
    for thing in key:
        checkLen(thing)
        for z in thing[0]:
            print(z)
        
