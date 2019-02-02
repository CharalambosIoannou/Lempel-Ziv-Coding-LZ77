import math
import time
import bitarray

def get_tuples(inp,lookahead_buffer_size , window_size):
    string_decode=[]
    d_bits=math.ceil(math.log(window_size,2))
    l_bits=math.ceil(math.log(lookahead_buffer_size,2))
    char_bits=8
    total_bits_needed= d_bits+l_bits+char_bits
    n=total_bits_needed
    for i in range (0, len(inp), n):
        tuples=inp[i:i+n]
        get_d_binary=tuples[0:d_bits]
        get_l_binary=tuples[d_bits:l_bits+d_bits]
        get_letter_binary=tuples[-8:]
        d_denary=int(get_d_binary,2)
        l_denary=int(get_l_binary,2)
        letter_denary=int(get_letter_binary,2)
        string_decode.append([d_denary,l_denary,letter_denary])
    #print(string_decode)
    return string_decode


def decompress(string_decode,lookahead_buffer_size , window_size):
    string=""
    for tuples in string_decode:
        #print(tuples)
        if (tuples[0] == 0):
            string=string+chr(tuples[2])
        else:
            let=string[-tuples[0] : - (tuples[0]-tuples[1]) ]
            string=string+let+chr(tuples[2])
    return string
            


lookahead_buffer_size=255
window_size=65535
inp="000000000000000000000000010000010000000000000000000000000100001000000000000000000000000001010010000000000000001100000001010000110000000000000010000000010100010000000000000001110000010000100000"
start= time.time()

a=get_tuples(inp,lookahead_buffer_size , window_size)   
b=decompress(a,lookahead_buffer_size , window_size)

final=time.time()
print("Total time: ", final - start)
print(b)
