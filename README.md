# lstm-chat-message-generator
A program that uses an LSTM model to generate artificial chat messages given a history of a user's speech patterns. Also known as the yikes_lolinator.

The current version will take in a path to a data location, train, and then generate some text based on the what it thinks a user may say.

# Things to be improved:
- Save checkpoints so that the model can be used for serving, also so that the program doesn't need to retrain each run.
- Sequence length of 3 may not be the most efficient
- Improve how batches are created
- Abstract some of the functions for robustness

# Usage
1. Download the code into a folder
2. Scrape a set of chat messages and put them in a .txt file
3. Run `python generator.py` with the chat location specified and number of epochs. (Use -h for specifics)
4. The program will train on the data provided and output some generated text upon completion

Output will look like this:
```
ITERATION: <total-1>/<total>
ITERATION: <total>/<total>
EPOCH: i, Loss = <LOSS>
Reading <file>
<predicted text>
```

Sample generation from a batch size of ~900 and 1 epoch on /test/chat_jack.txt:
```
ITERATION: 901/904
ITERATION: 902/904
ITERATION: 903/904
EPOCH: 0, Loss = Tensor("strided_slice:0", shape=(), dtype=float32)
Reading test/chat_jack.txt...
toy as came i ll in in i i i in in in wait wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait i get i in i in wait in wait
```

***For best results, use a consistent dataset of considerable scale with a reasonable number of epochs.***

