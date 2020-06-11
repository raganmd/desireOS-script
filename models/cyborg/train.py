from textgenrnn import textgenrnn

textgen = textgenrnn()

# reset training
textgen.reset()

# train from file
textgen.train_from_file('source/cyborg-text.txt', num_epochs=10)