# Discord specific code for converting JSON provided by https://dht.chylex.com/
# into a messages.txt file

import argparse, glob, sys, json, ast, copy
from random import shuffle

parser = argparse.ArgumentParser(prog="ship-movement",
                                 description="parse commands to the ship movement model")

parser.add_argument('src_path', metavar='path', type=str, help="Path to a specific use's chat dialogue")

args = parser.parse_args()
file = args.src_path
#files = glob.glob(args.src_path)

def parse_json(data):
    json_data = json.loads(data)
    return json_data

def print_msgs(json_data, channel_id, user_id):
    for msg in json_data["data"][channel_id]:
        #print(type(str(json_data["data"][channel_id][str(msg)]["u"])))
        #print(type(user_id))
        #print(str(json_data["data"][channel_id][str(msg)]["u"]) == user_id)
        if(str(json_data["data"][channel_id][str(msg)]["u"]) == user_id):
            print(json_data["data"][channel_id][str(msg)]["m"])


f = open(file, encoding="utf8")
print("Reading "+file+"...")

# File global variables
json_data = parse_json(f.read())

print_msgs(json_data, "148597885418602497", "8")