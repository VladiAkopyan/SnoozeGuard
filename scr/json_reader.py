import json

def readJson(path, point):
    with open(path, 'r') as f:
        data = json.load(f)

    return data[point]