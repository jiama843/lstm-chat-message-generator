# lstm-chat-message-generator
A program that uses an LSTM model to generate artificial chat messages given a history of a user's speech patterns. Also known as the yikes_lolinator.

The current version will take in a path to a data location, train, and then generate some text based on the what it thinks a user may say.

# Things to be improved:
- Save checkpoints so that the model can be used for serving, also so that the program doesn't need to retrain each run.
- Sequence length of 3 may not be the most efficient
- Improve how batches are made
- Abstract some of the functions for robustness

# Usage
1. Download the code into a folder
2. Scrape a set of chat messages and put them in a .txt file
3. Run `python generator.py` with the chat location specified and number of epochs. (Use -h for specifics)
4. The program will train on the data provided and output some generated text upon completion

***For best results, use a consistent dataset with a reasonable number of epochs.***

