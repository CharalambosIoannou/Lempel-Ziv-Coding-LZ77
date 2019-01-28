from bitarray import bitarray
import re

inp="Peter Piper picked a peck of pickled peppers;"
length_inp=len(inp)
position=0
found=[]

len_buffer=0
counter=0
Peter Piper picked a peck of pickled peppers;A peck of pickled peppers Peter Piper picked;If Peter Piper picked a peck of pickled peppers,Where's the peck of pickled peppers Peter Piper picked?”

while (position <=length_inp-1 ):
    if (inp[position] not in found):
        found.append(inp[position])
        nextLett=inp[position]
        position=position +1
        d=0
        length=0        
    else:       
        d=1
        #print("counter: ", counter)
        #print("position: ", position)        
        counter=position
        repeatedArray=[]
        while (inp[counter] in found):
            print("found: ", found)
            print("found letters: ", inp[counter])
            repeatedArray.append(inp[counter])
            counter=counter +1
            #print("counter: ", counter)
            if (counter == length_inp):
                break
        length=counter-position
        if (counter == length_inp):
            nextLett="-"
        else:
            nextLett=inp[counter]
        #print("length of keyword: " , length)
        print("next Letter: ", nextLett)
        joined=''.join(repeatedArray)
        found.append(joined)
        found.append(nextLett)
        if (len(repeatedArray) ==1):
            for i in range (position-1,-1,-1):
                #print("i ", inp[i])
                #print("p ", inp[position])
                if (inp[i] == inp[position]):
                    #print("d: ", d)
                    position=position+2
                    break
                else:
                    d=d+1
        else:
            
            #print(joined)
            find_str=inp.find(joined)
            #print("joined pos: " , )
            #print("counter: ", counter)            
            d=position- find_str
            position=position+length+1
            #print("position: ", position)
            #print("len: ", length_inp)

                
            
            

      
    #print("pos: " , position)
    print(d, " , " , length, " , ", nextLett)
        
            
        
            
    
