
# def find_str(s, char):
#     index = 0

#     if char in s:
#         c = char[0]
#         for ch in s:
#             if ch == c:
#                 if s[index:index+len(char)] == char:
#                     return index

#             index += 1

#     return -1

# def find(word,inp):
#     for position1,w in enumerate(inp):
#         if w == string_to_check:
#             total= position1 + 1
#             print(total )
#             return (total)
#         else:
#             return 0

# inp="ABRACADABRA"
# length_inp=len(inp)
# position=0
# found=[]
# dictionary=[]

# len_buffer=0
# counter=0
# while (position <=length_inp-1 ):
#     if (inp[position] not in found):
#         found.append(inp[position])
#         nextLett=inp[position]
#         position=position +1
#         d=0
#         length=0       
#         dictionary.append([0,0,nextLett])
#         print("(0,0,",nextLett,")") 
#     else:
#         print("old pos: ", position)
#         for i in range (position,length_inp):
#             print(inp[position:position + 1])
#             string_to_check = inp.rfind(inp[position:position + 1], 0, position)
#             print("pos of char: ",string_to_check) #POSITON OF CHARACTER
#             print("length of repeating: " , find(string_to_check,inp))
#             if (find(string_to_check,inp) == 0): 
#                 string_to_check=string_to_check[:-1]
#                 length_string_to_check=len(string_to_check)
#                 nextLett=inp[position+1]
#                 #print(string_to_check)
#                 #print("pos: " , position)
#                 print(position-count,",",length_string_to_check,",",nextLett)
#                 position=position+length_string_to_check+1
#                 print("new pos: ", position)
#                 dictionary.append([position-count,",",length_string_to_check,",",nextLett])
#             else:
#                 print(" else string : ", string_to_check) 
#                 print(" else length of repeating: " , find(string_to_check,inp))
#                 continue

def longest_common_substring(s1, s2):
   m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
   longest, x_longest = 0, 0
   for x in range(1, 1 + len(s1)):
       for y in range(1, 1 + len(s2)):
           if s1[x - 1] == s2[y - 1]:
               m[x][y] = m[x - 1][y - 1] + 1
               if m[x][y] > longest:
                   longest = m[x][y]
                   x_longest = x
           else:
               m[x][y] = 0
   return s1[x_longest - longest: x_longest]






def shift(pos):
    for i in range (pos,pos+lookahead):
        if (i == len(inp)):
            break
        else:
            lookahead_array.append(inp[i])
            lookahead_dict.append([inp[i],i])



    if (position>=1):
        for j in range (pos,pos-window,-1):
            if (j<0 or j==pos-window):
                break
            else:
                window_array.append(inp[j])
                #window_dict.append([inp[j],j])  
    window_array.reverse()
    return lookahead_array,lookahead_dict,window_array
#print(window_array)
#reversed(window_array)
inp="ABRACADABRAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
position = 0
window=20
lookahead=20
found_letter=[]
lookahead_array=[]
window_array=[]
lookahead_dict=[]

shift(0)
shift(3)

"""
    print("Current Position: " , position)
    if (position == 0 or inp[position] not in found_letter ):
        found_letter.append(inp[position])
        print("(0,0,",inp[position],")")
        del lookahead_array[0]
        del lookahead_dict[0]
        position= position + 1         
    else:
        break

        #break
      
""" 

    # while (len(lookahead_array) != 0):
    #     for j in range (0,len(lookahead_array)):
    #         if (lookahead_array[j] not in found_letter):
    #             found_letter.append(lookahead_array[j])
    #             print("(0,0,",lookahead_array[j],")")
    #         else:
    #             count = inp.rfind(inp[position:position + lookahead + 1], 0, position)
    #             print(count)
    #             break


    


        

            
        