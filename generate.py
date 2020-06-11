from textgenrnn import textgenrnn

textgen = textgenrnn()

textgen.generate_to_file('models/cyborg/outputs/output_05.txt', 
                        n=5, 
                        temperature=0.8)