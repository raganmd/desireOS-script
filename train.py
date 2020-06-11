from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.train_from_file('models/cyborg/cyborg-text.txt', num_ephocs=1)