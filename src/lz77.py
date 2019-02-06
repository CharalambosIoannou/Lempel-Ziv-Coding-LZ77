import time
import math
import bitarray
import sys



def get_binary(string_encoded,lookahead_buffer_size , window_size):
    full_string=""
    d_bits=math.ceil(math.log(window_size+1,2))
    l_bits=math.ceil(math.log(lookahead_buffer_size+1,2))
    char_bits=8
    total_bits_needed= d_bits+l_bits+char_bits
    d=""
    l=""
    next_lett=""
    for i in string_encoded:
        d="{0:b}".format(i[0]).zfill(d_bits)
        l="{0:b}".format(i[1]).zfill(l_bits)
        next_lett="{0:b}".format(i[2]).zfill(char_bits)
        full_string=full_string+d+l+next_lett
    #print("full: ",full_string)
    return full_string
        

def longest_match(inp, current_position,lookahead_buffer_size , window_size):
    positions_found=[]
    if (current_position + lookahead_buffer_size < len(inp) +1):
        look_ahead_buffer=current_position + lookahead_buffer_size
    else:
        look_ahead_buffer=len(inp)+1  

    for i in range(current_position+1 , look_ahead_buffer):
        if (i>len(inp)):
            break
        else:
            string_to_check=inp[current_position:i]
            if (current_position - window_size > 0):
                start_index=current_position - window_size
            else:
                start_index=0
            find_char=inp[start_index:current_position].rfind(string_to_check)
            if (find_char != -1):
                d=len(inp[start_index:current_position]) - find_char
                l=len(string_to_check)
                positions_found.append([d,l])
                
    if (len(positions_found) != 0 ):
        d=positions_found[-1][0]
        l=positions_found[-1][1]
        #print(d)
        #print(l)
        return d,l
    else:
        return -1,-1


def compress(file_name,lookahead_buffer_size,window_size):    
    try:
        input_file = open(file_name, 'rb')
        inp = input_file.read()
        inp_to_binary=bitarray.bitarray(endian='big')
        inp_to_binary.frombytes(inp)
    except IOError:
        print('Could not open file')
    length_original=len(inp_to_binary)
    print("Original length: " , length_original)
    string_encoded=[]
    position = 0
    aleady_found=[]
    while position < len(inp):    
        d,l=longest_match(inp,position,lookahead_buffer_size,window_size)
        if d == -1 and l== -1:
            aleady_found.append(inp[position])
            #print("( 0 , 0 ,",inp[position],")")
            string_encoded.append([0,0,inp[position]])
            position=position+1
        else:
            if (position +l == len(inp)):
                next_letter=32
            else:
                next_letter=inp[position+l]            
            #print("(",d,",",l,",",next_letter,")")
            string_encoded.append([d,l,next_letter])
            position=position+l+1
    #print(string_encoded)
    final_string=get_binary(string_encoded,lookahead_buffer_size, window_size)
    print("Compressed Length: ", len(final_string))
    print("Compression Ratio " , length_original/len(final_string))
    return final_string



def get_tuples(inp,lookahead_buffer_size , window_size):
    string_decode=[]
    d_bits=math.ceil(math.log(window_size+1,2))
    l_bits=math.ceil(math.log(lookahead_buffer_size+1,2))
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
    #print("decode: ",string_decode)
    return string_decode


def decompress(inp,lookahead_buffer_size , window_size):
    string_decode=get_tuples(inp,lookahead_buffer_size , window_size)
    final_string=""
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
            



time_array=[]
#window_size=[1,1,501,1001,1001,2001,2001,3001,3001,3001]
#lookahead_buffer_size=10
window_size=5
for i in range (1,30,1):
    print("Window Size: ",window_size )
    print("Buffer Size: ",i )
    print("_______Compress_______")
    print()
    start = time.time()
    final = compress("../tests/ABRACADABRA.txt", i, window_size)
    #print(final)
    finish = time.time()
    print()
    print("Compress Time taken: " ,finish-start)
    print("_______Decompress_______")
    print()
    start1= time.time()
    tuples_list=get_tuples(final,i , window_size)
    binary_string=get_binary(tuples_list,i , window_size)
    print(decompress(final,i , window_size))

    final1=time.time()
    decomp_time=final1 - start1
    print("Decompress Total time: ",decomp_time )
    time_array.append([window_size,i,decomp_time])
    sep = ""

    print("- - - - - - - - - - NEW EXPERIMENT- - - - - - - - - -")


with open('decomp.csv', 'w') as csv:
    for row in time_array:
        csv.write(sep.join(str(row)))
        csv.write("\n")


