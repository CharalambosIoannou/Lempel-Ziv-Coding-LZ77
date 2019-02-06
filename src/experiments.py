from lz77_compress import compress
from lz77_compress import get_original_length
from lz77_compress import get_compressed_length
from lz77_compress import get_string_encoded
from lz77_compress import get_binary
from lz77_compress import get_ratio
from lz77_decompress import get_tuples
from lz77_decompress import decompress
import sys
import time

############Const buffer
time_array_comp=[]
time_array_decomp=[]
#window_size=[1,1,501,1001,1001,2001,2001,3001,3001,3001]
lookahead_buffer_size=250
#window_size=4000
path="memetics.txt"
with open(path+'_compress_const_buffer.txt','w') as f:

    for i in range (1,6000,500):
        print("Window Size: ",i , file=f)
        print("Buffer Size: ",lookahead_buffer_size, file=f )
        print("__________________________________________Compress__________________________________________", file=f)
        print(file=f)
        start = time.time()
        final = compress("../tests/"+path, lookahead_buffer_size, i)
        print("Original length: " , get_original_length(), file=f)
        #print(get_string_encoded(), file=f)
        finish = time.time()
        print(file=f)
        comp_time=finish-start
        print("Compress Time taken: " ,comp_time, file=f)
        print("Compressed Length: ",get_compressed_length(), file=f )
        print("Compression Ratio " , get_ratio(), file=f )
        #print("__________________________________________Decompress__________________________________________", file=f)
        print(file=f)
        start1= time.time()
        #tuples_list=get_tuples(final,lookahead_buffer_size , i)
        string=decompress(final,lookahead_buffer_size , i)
        #print(string,file=f)
        final1=time.time()
        decomp_time=final1 - start1
        #print("Decompress Total time: ",decomp_time, file=f )
        time_array_comp.append([i,lookahead_buffer_size,comp_time])
        time_array_decomp.append([i,lookahead_buffer_size,decomp_time])
        
        print(file=f)
        

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - NEW EXPERIMENT- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", file=f)


sep = ""
with open('comp_const_buff.csv', 'w') as csv:
    for row in time_array_comp:
        csv.write(sep.join(str(row)))
        csv.write("\n")

sep = ""
with open('decomp_const_buff.csv', 'w') as csv:
    for row in time_array_decomp:
        csv.write(sep.join(str(row)))
        csv.write("\n")




print(2)

############Const window


time_array_comp=[]
time_array_decomp=[]
#window_size=[1,1,501,1001,1001,2001,2001,3001,3001,3001]
#lookahead_buffer_size=250
window_size=5000
with open(path+'_compress_const_window.txt','w') as f:

    for i in range (1,500,50):
        print("Window Size: ",window_size , file=f)
        print("Buffer Size: ",i, file=f )
        print("__________________________________________Compress__________________________________________", file=f)
        print(file=f)
        start = time.time()
        final = compress("../tests/"+path, i, window_size)
        print("Original length: " , get_original_length(), file=f)
        #print(get_string_encoded(), file=f)
        finish = time.time()
        print(file=f)
        comp_time=finish-start
        print("Compress Time taken: " ,comp_time, file=f)
        print("Compressed Length: ",get_compressed_length(), file=f )
        print("Compression Ratio " , get_ratio(), file=f )
        #print("__________________________________________Decompress__________________________________________", file=f)
        print(file=f)
        start1= time.time()
        #tuples_list=get_tuples(final,i , window_size)
        string=decompress(final,i , window_size)
        #print(string,file=f)
        final1=time.time()
        decomp_time=final1 - start1
        #print("Decompress Total time: ",decomp_time, file=f )
        time_array_comp.append([window_size,i,comp_time])
        time_array_decomp.append([window_size,i,decomp_time])
        print(file=f)
        

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - NEW EXPERIMENT- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", file=f)


sep = ""
with open('comp_const_wind.csv', 'w') as csv:
    for row in time_array_comp:
        csv.write(sep.join(str(row)))
        csv.write("\n")

sep = ""
with open('decomp_const_wind.csv', 'w') as csv:
    for row in time_array_decomp:
        csv.write(sep.join(str(row)))
        csv.write("\n")



print(3)


############Compress






time_array=[]
#window_size=[1,1,501,1001,1001,2001,2001,3001,3001,3001]
lookahead_buffer_size=250
#window_size=4000

with open(path+'_compress.txt','w') as f:

    for i in range (1,6000,500):
        print("Window Size: ",i , file=f)
        print("Buffer Size: ",lookahead_buffer_size, file=f )
        print("__________________________________________Compress__________________________________________", file=f)
        print(file=f)
        start = time.time()
        final = compress("../tests/"+path, lookahead_buffer_size, i)
        print("Original length: " , get_original_length(), file=f)
        print(final, file=f)
        finish = time.time()
        print(file=f)
        comp_time=finish-start
        print("Compress Time taken: " ,comp_time, file=f)
        print("Compressed Length: ",get_compressed_length(), file=f )
        print("Compression Ratio " , get_ratio(), file=f )
        #print("__________________________________________Decompress__________________________________________", file=f)
        print(file=f)
        start1= time.time()
        #tuples_list=get_tuples(final,lookahead_buffer_size , i)
        string=decompress(final,lookahead_buffer_size , i)
        #print(string,file=f)
        final1=time.time()
        decomp_time=final1 - start1
        #print("Decompress Total time: ",decomp_time, file=f )
        time_array.append([i,lookahead_buffer_size,comp_time])
        print(file=f)
        

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - NEW EXPERIMENT- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", file=f)









print(4)



############Const decompress












time_array=[]
#window_size=[1,1,501,1001,1001,2001,2001,3001,3001,3001]
lookahead_buffer_size=250
#window_size=4000
with open(path+'_decompress.txt','w') as f:

    for i in range (1,6000,500):
        print("Window Size: ",i , file=f)
        print("Buffer Size: ",lookahead_buffer_size, file=f )
        print("__________________________________________Compress__________________________________________", file=f)
        print(file=f)
        start = time.time()
        final = compress("../tests/"+path, lookahead_buffer_size, i)
        print("Original length: " , get_original_length(), file=f)
        print(final, file=f)
        finish = time.time()
        print(file=f)
        print("Compress Time taken: " ,finish-start, file=f)
        print("Compressed Length: ",get_compressed_length(), file=f )
        print("Compression Ratio " , get_ratio(), file=f )
        print("__________________________________________Decompress__________________________________________", file=f)
        print(file=f)
        start1= time.time()
        tuples_list=get_tuples(final,lookahead_buffer_size , i)
        binary=get_binary(tuples_list,lookahead_buffer_size , i)
        #string=decompress(final,lookahead_buffer_size , i)
        print(binary,file=f)
        #print(string,file=f)
        final1=time.time()
        decomp_time=final1 - start1
        print("Decompress Total time: ",decomp_time, file=f )
        time_array.append([i,lookahead_buffer_size,decomp_time])
        print(file=f)
        

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - NEW EXPERIMENT- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", file=f)



