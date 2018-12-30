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
        if(msg["t"] == user_id):
            print(msg["m"])

#for file in files:

# For each replay, train the model
f = open(file, "r")
print("Reading "+file+"...")

# Batch of 2d input tensors
input_batch = []
output_batch = []

# File global variables
json_data = parse_json(f.read())

print_msgs(json_data, "148597885418602497", "151521079486054400")