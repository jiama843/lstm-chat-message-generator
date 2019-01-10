import tensorflow as tf
#from data_provider import DataProvider
from lstm_model import LSTM_model
import numpy as np

# Hyperparameters
BATCH_SIZE = 32
SEQUENCE_LENGTH = 3
LEARNING_RATE = 0.01
#DECAY_RATE = 0.97
HIDDEN_LAYERS = 1000
CELLS_SIZE = 2



g = tf.Graph()
with g.as_default():
  # Operations created in this scope will be added to `g_1`.
  c = tf.constant("Node in g")

  # Sessions created in this scope will run operations from `g_1`.
  sess = tf.Session()

  # Replace 600 with a dynamic vocabulary length from data provider
  lstm_nn = LSTM_model(600, BATCH_SIZE, SEQUENCE_LENGTH, HIDDEN_LAYERS, CELLS_SIZE)