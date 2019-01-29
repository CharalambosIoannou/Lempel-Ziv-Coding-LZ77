def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1

def find(word,inp):
    for position1,w in enumerate(inp):
        if w == string_to_check:
            total= position1 + 1
            print(total )
            return (total)
        else:
            return 0

inp="ABRACADABRA"
length_inp=len(inp)
position=0
found=[]
dictionary=[]

len_buffer=0
counter=0
while (position <=length_inp-1 ):
    if (inp[position] not in found):
        found.append(inp[position])
        nextLett=inp[position]
        position=position +1
        d=0
        length=0       
        dictionary.append([0,0,nextLett])
        print("(0,0,",nextLett,")") 
    else:
        print("old pos: ", position)
        for i in range (position,length_inp):
            string_to_check= count = inp.rfind(inp[position:position + 1], 0, position)
            print(string_to_check) #POSITON OF CHARACTER
            print("length of repeating: " , find(string_to_check,inp))
            if (find(string_to_check,inp) == 0): 
                string_to_check=string_to_check[:-1]
                length_string_to_check=len(string_to_check)
                nextLett=inp[position+1]
                #print(string_to_check)
                #print("pos: " , position)
                print(position-count,",",length_string_to_check,",",nextLett)
                position=position+length_string_to_check+1
                print("new pos: ", position)
                dictionary.append([position-count,",",length_string_to_check,",",nextLett])
            else:
                print(" else string : ", string_to_check) 
                print(" else length of repeating: " , find(string_to_check,inp))
                continue

        

            
        