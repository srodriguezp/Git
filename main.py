import json
data_list = []
with open("data.json", "r") as file:
    for line in file:
        dict = json.dumps(line)
        data_list.append(dict)

def rets(data):
    tweets = []
    for tweet in data:
        pass

def users(data):
    pass

def days(data):
    pass

def hash(data):
    pass

def main():
    pass
