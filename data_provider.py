import argparse, glob, sys, json, ast, copy
from random import shuffle

parser = argparse.ArgumentParser(prog="ship-movement",
                                 description="parse commands to the ship movement model")

parser.add_argument('src_path', metavar='path', type=str, help="Path to a specific use's chat dialogue")

args = parser.parse_args()
files = glob.glob(args.src_path)

chat_dict = []

def txt_to_dict(phrase):

    chat_dict[phrase] += 1