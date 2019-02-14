from lz77 import main


path="../tests/memetics.txt" #change this variable to the path of the file to be tested
window_size=4000 #change this variable to the desired window size
lookahead_buffer_size=250 #change this variable to the desired lookahead buffer size

""" Run the program """


main(path,window_size,lookahead_buffer_size)

