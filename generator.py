import tensorflow as tf
from data_provider import generate_data
from lstm_model import LSTM_model
import numpy as np

# Hyperparameters
BATCH_SIZE = 32
SEQUENCE_LENGTH = 3
TARGET_LENGTH = 1
LEARNING_RATE = 0.01
HIDDEN_LAYERS = 1000

tensorboard_dir = "./data_summaries"

g = tf.Graph()
with g.as_default():
  # Operations created in this scope will be added to `g_1`.
  c = tf.constant("Node in g")

  # Sessions created in this scope will run operations from `g_1`.
  sess = tf.Session()

  summaries = tf.summary.merge_all()
  writer = tf.summary.FileWriter(tensorboard_dir)
  writer.add_graph(sess.graph)
  sess.run(tf.global_variables_initializer())

  # Replace 600 with a dynamic vocabulary length from data provider
  lstm_nn = LSTM_model(1, BATCH_SIZE, SEQUENCE_LENGTH, TARGET_LENGTH, HIDDEN_LAYERS)
  data = generate_data('test/chat_jack.txt')

  print(data)