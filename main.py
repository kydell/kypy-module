import call, json

data = call.pickit()

# temporary, to catch response and work with responses
# without having to call the API every single time
with open("thesaurus.json", "w") as ofile:
    json.dump(data, ofile)


