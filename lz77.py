def myFunct(data, current_position,inp,lookahead_buffer_size , window_size):
    letters_found=[]
    if (current_position + lookahead_buffer_size < len(data) +1):
        look_ahead_buffer=current_position + lookahead_buffer_size
    else:
        look_ahead_buffer=len(data)+1
    

    for i in range(current_position+1 , look_ahead_buffer):
        if (i>len(data)):
            break
        else:
            #print(current_position)
            #print(i)
            string_to_check=data[current_position:i]
            #print("str: " , string_to_check)
            if (current_position - window_size > 0):
                start_index=current_position - window_size
            else:
                start_index=0
            #print("wind: " , inp[start_index:current_position])
            find_char=inp[start_index:current_position].rfind(string_to_check)
            if (find_char != -1):
                #print(len(inp[start_index:current_position]) - find_char)
                #print(len(string_to_check))
                d=len(inp[start_index:current_position]) - find_char
                l=len(string_to_check)
                letters_found.append([d,l])
                
    #print("matched: " , ''.join(letters_found))
    if (len(letters_found) != 0 ):
        d=letters_found[-1][0]
        l=letters_found[-1][1]
        #print(d)
        #print(l)
        return d,l
    else:
        return -1,-1


def encode(inp,lookahead_buffer_size,window_size):
    string_encoded=[]
    position = 0
    #inp = "Peter Piper picked a peck of pickled peppers;A peck of pickled peppers Peter Piper picked;If Peter Piper picked a peck of pickled peppers,Where's the peck of pickled peppers Peter Piper picked"
    #inp="Peter Piper picked a peck of pickled peppers;A peck of pickled peppers Peter Piper picked;If Peter Piper picked a peck of pickled peppers,Where's the peck of pickled peppers Peter Piper picked?"
    aleady_found=[]
    while position < len(inp):
        d,l=myFunct(inp,position,inp,lookahead_buffer_size,window_size)
        if d == -1 and l== -1:
            aleady_found.append(inp[position])
            #print("( 0 , 0 ,",inp[position],")")
            string_encoded.append([0,0,inp[position]])
            position=position+1
        else:
            if (position +l == len(inp)):
                next_letter="-"
            else:
                next_letter=inp[position+l]            
            #print("(",d,",",l,",",next_letter,")")
            string_encoded.append([d,l,next_letter])
            position=position+l+1
    return string_encoded

inp="ABRACADABRA"
lookahead_buffer_size=15
window_size=15
enc = encode(inp,lookahead_buffer_size,window_size)
print(enc)