import tensorflow as tf
from data_provider import generate_data
from lstm_model import LSTM_model
import numpy as np

# Hyperparameters
BATCH_SIZE = 1
SEQUENCE_LENGTH = 3
TARGET_LENGTH = 1
LEARNING_RATE = 0.001
DECAY_RATE = 0.97
HIDDEN_LAYERS = 1000

tensorboard_dir = "./data_summaries"

def train_lstm(sess):
  #g = tf.Graph()
  #with g.as_default():
    # Operations created in this scope will be added to `g_1`.
   # c = tf.constant("Node in g")

  # Replace 600 with a dynamic vocabulary length from data provider
  lstm_nn = LSTM_model(1, BATCH_SIZE, SEQUENCE_LENGTH, TARGET_LENGTH, HIDDEN_LAYERS)
  data = generate_data('test/chat_jack.txt')

  # Sessions created in this scope will run operations from `g_1`.
  summaries = tf.summary.merge_all()
  writer = tf.summary.FileWriter(tensorboard_dir)
  writer.add_graph(sess.graph)
  sess.run(tf.global_variables_initializer())

  #sess.run(lstm_nn.learning_rate)
  inputs, targets = data[0], data[1]
  for i in range(len(inputs)):
    print("ITERATION: "+ str(i))
    feed = {lstm_nn.inputs: [inputs[i]], lstm_nn.targets: [targets[i]]}

    sess.run(lstm_nn.train_step, feed)

def text_gen(sess, input, length):
  # Shift batches based on initial input to continue generating text
  curr_input = input
  data = generate_data('test/chat_jack.txt')

  for i in range(0, length):
    lstm_nn = LSTM_model(1, BATCH_SIZE, SEQUENCE_LENGTH, TARGET_LENGTH, HIDDEN_LAYERS, training=False)
    word = lstm_nn.predict_word(sess, curr_input, data[2])
    print(word)

    # This needs to be customized based on SEQUENCE_LENGTH later on
    curr_input = [curr_input[1], curr_input[2], word]

sess = tf.Session()
train_lstm(sess)
text_gen(sess, ["oh", "oh", "Oh"], 20)