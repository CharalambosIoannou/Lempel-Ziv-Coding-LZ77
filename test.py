def findLongestMatch(data, current_position):
    """ 
    Finds the longest match to a substring starting at the current_position 
    in the lookahead buffer from the history window
    """
    end_of_buffer = min(current_position + lookahead_buffer_size, len(data) + 1)
    best_match_distance = -1
    best_match_length = -1

    # Optimization: Only consider substrings of length 2 and greater, and just 
    # output any substring of length 1 (8 bits uncompressed is better than 13 bits
    # for the flag, distance, and length)
    for j in range(current_position , end_of_buffer):

        start_index = max(0, current_position - window_size)
        substring = data[current_position:j]
        print("sub ", substring)

        for i in range(start_index, current_position):

            repetitions = len(substring) / (current_position - i)

            last = len(substring) % (current_position - i)

            matched_string = data[i:current_position] * int(repetitions) + data[i:i+last]
            if matched_string == substring and len(substring) > best_match_length:
                best_match_distance = current_position - i 
                best_match_length = len(substring)

    if best_match_distance > 0 and best_match_length > 0:
        return (best_match_distance, best_match_length)
    return None


def myFunct(data, current_position):
    letters_to_check=[]
    look_ahead_buffer=min(current_position + lookahead_buffer_size, len(data) + 1)
    best_match_distance = -1
    best_match_length = -1
    for j in range(current_position , look_ahead_buffer):
        if (j>=len(data)):
            break
        else:
            string_to_check=data[j]
            letters_to_check.append(string_to_check)
    #print(letters_to_check)
    string_to_compare=data[:-len(letters_to_check)]
    letters_to_check_string=''.join(letters_to_check)
    print("str " , letters_to_check_string)
    #print(string_to_compare)
    for i in range (0,len(letters_to_check)):
        if (letters_to_check_string) in string_to_compare:
            #print("Let: " , letters_to_check_string)
            #print("length: " , len(letters_to_check_string))
            pos_in_data=string_to_compare.find(letters_to_check_string)
            #print("Pos: ",current_position - pos_in_data)
            #print("True")
            print(current_position - pos_in_data ,",",len(letters_to_check_string) )
            break
        else:
            print(letters_to_check_string[:-i])
            if (letters_to_check_string[:-i]) in string_to_compare:
                #print("Let: " , letters_to_check_string[:-i])
                #print("length: " , len(letters_to_check_string))
                #print("Pos: ",current_position - pos_in_data)
                pos_in_data=string_to_compare.find(letters_to_check_string)
                print(current_position - pos_in_data ,",",len(letters_to_check_string) )
                #print("True")
                
            
        
            




        
lookahead_buffer_size=15
window_size=15
print(findLongestMatch("ABRACADABRA",5))
print(myFunct("ABRACADABRA",5))
