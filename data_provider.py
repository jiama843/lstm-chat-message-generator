import argparse, glob, sys, json, ast, copy
from random import shuffle

parser = argparse.ArgumentParser(prog="ship-movement",
                                 description="parse commands to the ship movement model")

parser.add_argument('src_path', metavar='path', type=str, help="Path to a specific use's chat dialogue")

args = parser.parse_args()
files = glob.glob(args.src_path)

chat_dict = {}

def txt_to_dict(phrase):
    #split phrase into arr, and for each, add to dictionary
    word_arr = phrase.split()
    for word in word_arr:
        if (word in chat_dict):
            chat_dict[word] += 1
        else:
            chat_dict[word] = 1

for file in files:
    # For each replay, train the model
    f = open(file, "r")
    print("Reading "+file+"...")

    txt_to_dict(f.read())

print(chat_dict)