import argparse, glob, sys, json, ast, copy
import random
import tensorflow as tf
from data_provider import generate_data
from lstm_model import LSTM_model
import numpy as np

parser = argparse.ArgumentParser(prog="yikes_lolintator",
                                 description="Send a sample text file to the yikes lolinator")

parser.add_argument('src_path', metavar='path', type=str, help="Path to a specific user's chat dialogue (.txt)")

args = parser.parse_args()
files = glob.glob(args.src_path)
file_path = files[0]

data = generate_data(file_path)

# Hyperparameters
BATCH_SIZE = 1
SEQUENCE_LENGTH = 3
TARGET_LENGTH = len(data[2][0])
LEARNING_RATE = 0.001
DECAY_RATE = 0.97
HIDDEN_LAYERS = 1000

epochs = 1

tensorboard_dir = "./data_summaries"

def train_lstm(sess):

  data = generate_data(file_path)
  lstm_nn = LSTM_model(len(data[2][0]), BATCH_SIZE, SEQUENCE_LENGTH, TARGET_LENGTH, len(data[2][0]))

  # Sessions created in this scope will run operations from `g_1`.
  summaries = tf.summary.merge_all()
  writer = tf.summary.FileWriter(tensorboard_dir)
  writer.add_graph(sess.graph)
  sess.run(tf.global_variables_initializer())

  #sess.run(lstm_nn.learning_rate)
  inputs, targets = data[0], data[1]
  for j in range(0, epochs):
    for i in range(len(inputs)):
      print("ITERATION: "+str(i)+"/"+str(len(inputs)))
      feed = {lstm_nn.inputs: [inputs[i]], lstm_nn.targets: [targets[i]]}

      sess.run(lstm_nn.train_step, feed)
    print("EPOCH: " + str(j) + ", Loss = " + str(lstm_nn.cost[-1]))

def text_gen(sess, input, length):
  # Shift batches based on initial input to continue generating text
  curr_input = input
  data = generate_data(file_path)

  phrase = ""
  for i in range(0, length):
    lstm_nn = LSTM_model(len(data[2][0]), BATCH_SIZE, SEQUENCE_LENGTH, TARGET_LENGTH, len(data[2][0]), training=False)
    word = lstm_nn.predict_word(sess, curr_input, data[2])
    phrase += word + " "

    # This needs to be customized based on SEQUENCE_LENGTH later on
    curr_input = [curr_input[1], curr_input[2], word]
  print(phrase)

sess = tf.Session()
train_lstm(sess)
text_gen(sess, [data[2][1][random.randint(0, TARGET_LENGTH - 1)],
                data[2][1][random.randint(0, TARGET_LENGTH - 1)],
                data[2][1][random.randint(0, TARGET_LENGTH - 1)]], 300)