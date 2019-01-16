# lstm-chat-message-generator
A program that uses LSTM models to generate artificial chat messages given a history of a user's speech patterns. Also known as the yikes_lolinator.

# Things to be improved:
- Save checkpoints so that the model can be used for serving
- Abstract some of the functions for robustness

# Usage
1. Download the code into a folder
2. Scrape a set of chat messages and put them in a .txt file
3. Run `python generator.py` with the chat location specified
4. The program will train on the data provided and output some generated text upon completion
