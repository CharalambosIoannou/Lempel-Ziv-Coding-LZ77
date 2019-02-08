import time
import math
import bitarray

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
    global length_original
    global string_encoded
    global comp_length
    try:
        input_file = open(file_name, 'rb')
        inp = input_file.read()
        #print("inp:",inp)
        inp_to_binary=bitarray.bitarray(endian='big')
        inp_to_binary.frombytes(inp)
        #print("inp bin: ", inp_to_binary)
    except IOError:
        print('Could not open file')
    #global length_original
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
    comp_length=len(final_string)
    print("Compressed Length: ",comp_length )
    global ratio
    ratio = length_original/len(final_string)
    print("Compression Ratio " , ratio )
    return final_string




def get_ratio():
    return ratio
def get_original_length():
    return length_original
def get_compressed_length():
    return comp_length
def get_string_encoded():
    return string_encoded


"""
lookahead_buffer_size=20
window_size=20


print("##### Compress #####")
print()
start = time.time()

final = compress("../tests/ABRACADABRA.txt", lookahead_buffer_size, window_size)
print(final)

finish = time.time()
print(finish-start)
print("Time taken: " ,finish-start)
f = open("binary.txt", "w")
f.write(final) 
"""

