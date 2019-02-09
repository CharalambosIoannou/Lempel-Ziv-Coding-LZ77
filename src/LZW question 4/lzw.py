"""
    code was taken from: https://rosettacode.org/wiki/LZW_compression#Python

"""
import math
import time
def compress(uncompressed):
    """Compress a string to a list of output symbols."""
 
    # Build the dictionary.
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    # in Python 3: dictionary = {chr(i): i for i in range(dict_size)}
 
    w = ""
    result = []
    for c in uncompressed:
        print("w ", w)
        print("c ", c)
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
 
    # Output the code for w.
    if w:
        result.append(dictionary[w])

    return result
 
 
def decompress(compressed):
    """Decompress a list of output ks to a string."""
    from io import StringIO
 
    # Build the dictionary.
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))
    # in Python 3: dictionary = {i: chr(i) for i in range(dict_size)}
 
    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)
 
        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
 
        w = entry
    return result.getvalue()
 
 
# How to use:


start=time.time()
input_file = open("../../tests/22.txt")
inp = input_file.read()
org_len=len(inp)*8
print("Original length: " ,org_len )
compressed = compress(inp)
print("max:",max(compressed))
comp_length=len(compressed) * math.ceil(math.log(max(compressed)+1,2))
print ("Compressed Length :",comp_length)
print("Compression Ratio: ",org_len/comp_length)
#print()
decompressed = decompress(compressed)
finish=time.time()
print("Time taken to compress: " , finish - start)
#print (decompressed)
