from lz77 import compress
from lz77 import get_original_length
from lz77 import get_compressed_length
from lz77 import get_string_encoded
from lz77 import get_binary
from lz77 import get_ratio
from lz77 import get_tuples
from lz77 import decompress
import sys
import time


path="abracadabra.txt"

window_size=5000 #constant window size used in experiment 1
lookahead_buffer_size=300 #constant buffer size used in experiment 2,3,4





"""
    Experiment: 1 - Constant window size  
"""   

time_array=[]
with open(path+'_compress_const_window.txt','w') as f:
    for i in range (1,300,10):
        print("Window Size: ",window_size , file=f)
        print("Buffer Size: ",i, file=f )
        print("____________________________________________________________________________________Compress____________________________________________________________________________________", file=f)
        print(file=f)
        start = time.time()
        final = compress(path, i, window_size)
        print("Original length: " , get_original_length(), file=f)
        finish = time.time()
        print(file=f)
        comp_time=finish-start
        print("Compress Time taken: " ,comp_time, file=f)
        print("Compressed Length: ",get_compressed_length(), file=f )
        print("Compression Ratio " , get_ratio(), file=f )
        print("____________________________________________________________________________________Decompress____________________________________________________________________________________", file=f)
        print(file=f)
        start1= time.time()
        tuples_list=get_tuples(final,i , window_size)
        binary=get_binary(tuples_list,i , window_size)
        final1=time.time()
        decomp_time=final1 - start1
        print("Decompress Total time: ",decomp_time, file=f )
        time_array.append([window_size,i,decomp_time])
        print(file=f)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - NEW EXPERIMENT - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", file=f)

#output decompression time to an excel spreadsheet in order to get the values easier and produce graphs
"""
sep = ""
with open(path+'_decomp_const_window.csv', 'w') as csv:
    for row in time_array:
        csv.write(sep.join(str(row)))
        csv.write("\n")

"""

####################################################################

"""
    Experiment: 2 - Constant buffer size  
"""
     

time_array=[]
with open(path+'_compress_const_buffer.txt','w') as f:
    for i in range (1,5000,200):
        print("Window Size: ",i , file=f)
        print("Buffer Size: ",lookahead_buffer_size, file=f )
        print("____________________________________________________________________________________Compress____________________________________________________________________________________", file=f)
        print(file=f)
        start = time.time()
        final = compress(path, lookahead_buffer_size, i)
        print("Original length: " , get_original_length(), file=f)
        finish = time.time()
        print(file=f)
        print("Compress Time taken: " ,finish-start, file=f)
        print("Compressed Length: ",get_compressed_length(), file=f )
        print("Compression Ratio " , get_ratio(), file=f )
        print("____________________________________________________________________________________Decompress____________________________________________________________________________________", file=f)
        print(file=f)
        start1= time.time()
        tuples_list=get_tuples(final,lookahead_buffer_size , i)
        binary=get_binary(tuples_list,lookahead_buffer_size , i)
        final1=time.time()
        decomp_time=final1 - start1
        print("Decompress Total time: ",decomp_time, file=f )
        time_array.append([i,lookahead_buffer_size,decomp_time])
        print(file=f)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - NEW EXPERIMENT - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", file=f)

"""
sep = ""
with open(path+'_decomp_const_buffer.csv', 'w') as csv:
    for row in time_array:
        csv.write(sep.join(str(row)))
        csv.write("\n")
"""
####################################################################


"""
    Experiment: 3 - Compress File 
"""
     

time_array=[]
lookahead_buffer_size=300
with open(path+'_compress.txt','w') as f:
    for i in range (1,5000,200):
        print("Window Size: ",i , file=f)
        print("Buffer Size: ",lookahead_buffer_size, file=f )
        print("____________________________________________________________________________________Compress____________________________________________________________________________________", file=f)
        print(file=f)
        start = time.time()
        final = compress(path, lookahead_buffer_size, i)
        print("Original length: " , get_original_length(), file=f)
        print("Compressed Bits: " ,final, file=f)
        finish = time.time()
        print(file=f)
        comp_time=finish-start
        print("Compress Time taken: " ,comp_time, file=f)
        print("Compressed Length: ",get_compressed_length(), file=f )
        print("Compression Ratio " , get_ratio(), file=f )
        time_array.append([i,lookahead_buffer_size,comp_time])
        print(file=f)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - NEW EXPERIMENT - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", file=f)


"""
    Experiment: 4 - Decompress File 
"""

time_array=[]
with open(path+'_decompress.txt','w') as f:
    for i in range (1,5000,200):
        print("Window Size: ",i , file=f)
        print("Buffer Size: ",lookahead_buffer_size, file=f )
        print("____________________________________________________________________________________Compress____________________________________________________________________________________", file=f)
        print(file=f)
        start = time.time()
        final = compress(path, lookahead_buffer_size, i)
        print("Original length: " , get_original_length(), file=f)
        print("Compressed Bits: " ,final, file=f)
        finish = time.time()
        print(file=f)
        print("Compress Time taken: " ,finish-start, file=f)
        print("Compressed Length: ",get_compressed_length(), file=f )
        print("Compression Ratio " , get_ratio(), file=f )
        print("____________________________________________________________________________________Decompress____________________________________________________________________________________", file=f)
        print(file=f)
        start1= time.time()
        if (path[-3:] == "txt"):
            string=decompress(final,lookahead_buffer_size , i)
            print("Decompressed String: " , string,file=f)
            tuples_list=get_tuples(final,lookahead_buffer_size , i)
            binary=get_binary(tuples_list,lookahead_buffer_size , i)            
        else:            
            tuples_list=get_tuples(final,lookahead_buffer_size , i)
            binary=get_binary(tuples_list,lookahead_buffer_size , i)
            print("Decompressed Bits: ",binary,file=f)
        final1=time.time()
        decomp_time=final1 - start1
        print(file=f)
        print("Decompress Total time: ",decomp_time, file=f )
        print(file=f)
        if (final == binary):
            print ("Compression and Decompression MATCH",file=f)
        else:
            print ("Compression and Decompression DO NOT MATCH",file=f)
        time_array.append([i,lookahead_buffer_size,decomp_time])
        print(file=f)      
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - NEW EXPERIMENT - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", file=f)


