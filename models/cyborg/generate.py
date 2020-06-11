from textgenrnn import textgenrnn

textgen = textgenrnn()

textgen.generate_to_file('outputs/output_02.txt', 
                        n=5, 
                        temperature=0.8)