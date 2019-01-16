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
        learning_rate = 0.001,
        decay_rate = 0.97,
        training=True):

        self.word_count = vocabulary_size

        self.inputs = tf.placeholder(tf.float32, shape=(batch_size, sequence_length))
        self.targets = tf.placeholder(tf.int32, shape=(batch_size, target_length))

        self.learning_rate = learning_rate
        self.decay_rate = decay_rate

        rnn_cell = rnn.MultiRNNCell([rnn.LSTMCell(num_hidden_layers), rnn.LSTMCell(num_hidden_layers)])

        self.cell = rnn_cell

        with tf.variable_scope("rnn", reuse=tf.AUTO_REUSE):
            softmax_layer = tf.get_variable("softmax_layer", [num_hidden_layers, vocabulary_size])
            softmax_bias = tf.get_variable("softmax_bias", [vocabulary_size])

        with tf.variable_scope("rnn", reuse=tf.AUTO_REUSE):
            inputs = self.inputs

        inputs = tf.split(inputs, sequence_length, 1)

        #print(inputs)

        with tf.variable_scope("rnn", reuse=tf.AUTO_REUSE):
            outputs, states = rnn.static_rnn(rnn_cell, inputs, dtype=tf.float32)
            output = outputs[-1]#tf.reshape(tf.concat(outputs, 1), [-1, num_hidden_layers])

        self.logits = tf.matmul(output, softmax_layer) + softmax_bias
        self.probabilities = tf.nn.softmax(self.logits)

        #loss = tf.losses.sparse_softmax_cross_entropy(labels=self.targets, logits=self.logits)
        loss = tf.keras.backend.categorical_crossentropy(self.targets, self.logits, from_logits=True)
        self.cost = loss

        with tf.variable_scope("optimizer", reuse=tf.AUTO_REUSE):
            optimizer = tf.train.AdamOptimizer(self.learning_rate)
            self.train_step = optimizer.minimize(self.cost)

        tf.summary.histogram("logits", self.logits)
        tf.summary.histogram("probabilities", self.probabilities)
        tf.summary.histogram("loss", loss)

    def predict_word(self, sess, input, chat_dict):
        feed_in = []
        for _word in input:
            feed_in.append(chat_dict[0][_word])

        feed = {self.inputs: [feed_in] }
        probabilities = sess.run(self.probabilities, feed)

        probability = probabilities[0]
        word = chat_dict[1][probability[0]]
        return word
