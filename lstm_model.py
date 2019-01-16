import tensorflow as tf
from tensorflow.contrib import rnn

import numpy as np
sess = tf.InteractiveSession()

class LSTM_model:

    def __init__(
        self,
        vocabulary_size,
        batch_size,
        sequence_length,
        target_length,
        num_hidden_layers,
        training=True):

        self.word_count = vocabulary_size
        self.inputs = tf.placeholder(tf.float32, shape=(batch_size, sequence_length))
        self.targets = tf.placeholder(tf.int32, shape=(batch_size, target_length))

        #print(self.inputs)
        #print(self.targets)

        rnn_cell = rnn.LSTMCell(num_hidden_layers)
        self.cell = rnn_cell

        #print(rnn_cell.output_size)

        with tf.variable_scope("rnn", reuse=tf.AUTO_REUSE):
            softmax_layer = tf.get_variable("softmax_layer", [num_hidden_layers, vocabulary_size])
            softmax_bias = tf.get_variable("softmax_bias", [vocabulary_size])

        with tf.variable_scope("rnn", reuse=tf.AUTO_REUSE):
            inputs = self.inputs

        inputs = tf.split(inputs, sequence_length, 1)

        print(inputs)

        with tf.variable_scope("rnn", reuse=tf.AUTO_REUSE):
            outputs, states = rnn.static_rnn(rnn_cell, inputs, dtype=tf.float32)
            output = outputs[-1]#tf.reshape(tf.concat(outputs, 1), [-1, num_hidden_layers])

        print(outputs)
        print(states)
        print(output)

        self.logits = tf.matmul(output, softmax_layer) + softmax_bias
        self.probabilities = tf.nn.softmax(self.logits)
        #self.probabilities =

        print(self.logits)
        print(self.targets)

        loss = tf.losses.sparse_softmax_cross_entropy(labels=self.targets, logits=self.logits)

        tf.summary.histogram("logits", self.logits)
        tf.summary.histogram("probabilitiess", self.probabilities)
        tf.summary.histogram("loss", loss)
