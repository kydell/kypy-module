import call, json

data = call.pickit()

with open("response.json", "w") as ofile:
    json.dump(data, ofile)


