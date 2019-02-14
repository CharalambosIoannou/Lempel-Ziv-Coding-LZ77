import time
import math
import bitarray
import sys

"""
    Compression Starts Here
"""

#Returns the binary string of the tuples created from compressing the input file
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
    return full_string
        
#function that finds the longest possible match in the string starting from the current position
#and comparing the string in the lookahead buffer with the string in the window
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

        return d,l
    else:
        return -1,-1

#function that compresses the string into tuples using lz77 method and then converting the tuples to binary
def compress(file_name,lookahead_buffer_size,window_size):    
    global length_original
    global string_encoded
    global comp_length
    try:
        input_file = open(file_name, 'rb')
        inp = input_file.read()
        inp_to_binary=bitarray.bitarray(endian='big')
        inp_to_binary.frombytes(inp)
        #print("inp: ",inp_to_binary)
        length_original=len(inp_to_binary)
        print("Original length: " , length_original)
    except IOError:
        print('Could not open file')
        return
    except UnboundLocalError:
        print('Could not open file')
        return
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
    comp_length=len(final_string)
    global ratio
    ratio = length_original/comp_length
    print("Compressed Length: ", comp_length)
    print("Compression Ratio " , ratio)
    return final_string

"""
    Compression Ends Here
    Decompression Starts Here
"""

#function to convert binary back to tuples
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


#function that gets the tuples and converts them to the actual string
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

            
#get functions that are used in the experiments.py file to pass on variable values
def get_ratio():
    return ratio
def get_original_length():
    return length_original
def get_compressed_length():
    return comp_length
def get_string_encoded():
    return string_encoded


def main(path,window_size,lookahead_buffer_size):
    time_array=[] #array to store the compression or the decompression time. This is adjusted accordingly to the experiment that i want to make
    #constant values for the window and bufer size. Two of the most ideal values

    print("Window Size: ",window_size )
    print("Buffer Size: ",lookahead_buffer_size )
    print("_____________________________Compress_____________________________")
    print()
    start = time.time()
    final = compress(path, lookahead_buffer_size, window_size)
    if (final is None):
        print("Please enter a valid file name")
        return 
    else:
        print("Compressed Bits: " ,final)
        finish = time.time()
        print()
        print("Compress Time taken: " ,finish-start)
        print("_____________________________Decompress_____________________________")
        print()
        start1= time.time()
        if (path[-3:] == "txt"):
            string=decompress(final,lookahead_buffer_size , window_size)
            print("Decompressed String: ",string)
            tuples_list=get_tuples(final,lookahead_buffer_size , window_size)
            binary=get_binary(tuples_list,lookahead_buffer_size , window_size)
        else:            
            tuples_list=get_tuples(final,lookahead_buffer_size , window_size)
            binary=get_binary(tuples_list,lookahead_buffer_size , window_size)
            print("Decompressed Bits: ",binary)
        final1=time.time()
        decomp_time=final1 - start1
        print("Decompress Total time: ",decomp_time )
        if (final == binary):
            print ("Compression and Decompression MATCH")
        else:
            print ("Compression and Decompression DO NOT MATCH")
        time_array.append([window_size,lookahead_buffer_size,decomp_time])

        print("- - - - - - - - - - - - - NEW EXPERIMENT - - - - - - - - - - - - -")
    return binary


