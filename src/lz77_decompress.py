import math
import time
import bitarray

def get_tuples(inp,lookahead_buffer_size , window_size):
    string_decode=[]
    d_bits=math.ceil(math.log(window_size+1,2))
    l_bits=math.ceil(math.log(lookahead_buffer_size+1,2))
    char_bits=8
    total_bits_needed= d_bits+l_bits+char_bits
    for i in range (0, len(inp), total_bits_needed):
        tuples=inp[i:i+total_bits_needed]
        get_d_binary=tuples[0:d_bits]
        get_l_binary=tuples[d_bits:l_bits+d_bits]
        get_letter_binary=tuples[-8:]
        d_denary=int(get_d_binary,2)
        l_denary=int(get_l_binary,2)
        letter_denary=int(get_letter_binary,2)
        string_decode.append([d_denary,l_denary,letter_denary])
    #print(string_decode)
    return string_decode


def decompress(inp,lookahead_buffer_size , window_size):
    string_decode=get_tuples(inp,lookahead_buffer_size , window_size)
    final_string=""
    print("Length of tuples: ", len(string_decode))
    for tuples in string_decode:
        #print(tuples)
        if (tuples[0] == 0):
            final_string=final_string+chr(tuples[2])
        else:
            start_repeating=len(final_string)-tuples[0]
            end_repeating=len(final_string)-tuples[0]+tuples[1]            
            repeated_string=final_string[start_repeating:end_repeating]
            next_letter=chr(tuples[2])
            final_string=final_string+repeated_string+next_letter
    return final_string
            
"""

lookahead_buffer_size=20
window_size=20
inp="000000000001000001000000000001000010000000000001010010000110000101000011000100000101000100001110010000100000"
start= time.time()
#a=get_tuples(inp,lookahead_buffer_size , window_size)   
b=decompress(inp,lookahead_buffer_size , window_size)

final=time.time()
print("Total time: ", final - start)
print(b)
"""

