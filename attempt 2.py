import time
def find_in_dict(buffer, dictionary):
    shift = len(dictionary)
    substring = ""

    for character in buffer:
        substring_tmp = substring + character
        shift_tmp = dictionary.rfind(substring_tmp)

        if shift_tmp < 0:
            break

        substring = substring_tmp
        shift = shift_tmp

    return len(substring), len(dictionary) - shift
# Input inp
#inp = "Peter Piper picked a peck of pickled peppers.A peck of pickled peppers Peter Piper picked.If Peter Piper picked a peck of pickled peppers,Where's the peck of pickled peppers Peter Piper picked"
inp="ABRACADABRA"
# Get time
delta0 = time.time()

position = 0

found_chars = []
while position < len(inp) :    
    look_ahead_buffer = 0
    temp = -1
    #count = -1
    found = False
    for i in range(position, len(inp)):

        count = inp.rfind(inp[position:position + look_ahead_buffer + 1], 0, position)
        count1,count2 = find_in_dict(inp[position:position + look_ahead_buffer + 1],inp)
        print(count)
        print(count1)
        print(count2)
        if count == -1:
            break
        if count >= 0:
            look_ahead_buffer += 1
            temp = count
            found = True
    
    if (found == False):
        next_letter= inp[position]
        print("(0,0," , inp[position],  ")")
        found_chars.append([0, 0, next_letter])
        position = position + 1        
    else:
        
        if position + look_ahead_buffer <= len(inp):
            if (position+look_ahead_buffer == len(inp)):
                next_letter="-"
            else:
                next_letter = inp[position + look_ahead_buffer]
            print("(",','.join([str(position - temp),str( look_ahead_buffer), next_letter ]),")")
            found_chars.append([position - temp, look_ahead_buffer, next_letter ])
            position = position+ look_ahead_buffer + 1            
            
        else:
            print([position - temp, look_ahead_buffer , inp[position + look_ahead_buffer-1 ]])
            found_chars.append([position - temp, look_ahead_buffer , inp[position + look_ahead_buffer-1 ]])            
            break



delta1 = time.time()

print ("Old inp: " + inp)

print ("Compressed file size: " + "{:.2f}".format(3 * float(len(found_chars)) / len(inp) * 100) + "%")
print ("Elapsed time: " + "{:.5f}".format((delta1 - delta0)*100) + "ms")
