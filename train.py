from textgenrnn import textgenrnn

textgen = textgenrnn()

# reset training
# textgen.reset()

# train from file
textgen.train_from_largetext_file('models/cyborg/source/cyborg-text.txt',
                        new_model=True,
                        num_epochs=100,
                        word_level=True,
                        max_length=40,
                        max_gen_length=100,
                        max_words=5000)