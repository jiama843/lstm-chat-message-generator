import argparse, glob, sys, json, ast, copy
from random import shuffle

parser = argparse.ArgumentParser(prog="ship-movement",
                                 description="parse commands to the ship movement model")

parser.add_argument('src_path', metavar='path', type=str, help="Path to a specific use's chat dialogue")

args = parser.parse_args()
files = glob.glob(args.src_path)

def txt_to_dict(phrase):
    chat_dict = {}
    #split phrase into arr, and for each, add to dictionary
    word_arr = phrase.split()
    for word in word_arr:
        if (word in chat_dict):
            chat_dict[word] += 1
        else:
            chat_dict[word] = 1
    return chat_dict

def data_provider(word_dict):
    word_id = 0
    sorted_word_keys = sorted(word_dict, key=word_dict.get, reverse=True)

    dictionary = {}
    for key in sorted_word_keys:
        dictionary[key] = word_id
        word_id += 1

    reverse_dictionary = dict(zip(word_dict.values(), word_dict.keys()))
    return [dictionary, reverse_dictionary]

for file in files:
    # For each replay, train the model
    f = open(file, "r")
    print("Reading "+file+"...")

    chat_dict = txt_to_dict(f.read())
    data_dictionary = data_provider(chat_dict)

print(data_dictionary)