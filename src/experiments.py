from lz77_compress import compress
from lz77_compress import get_ratio
#from lz77_decompress import decompress
import time

window_size=[]
buffer_size=[]
ratio=[]
time_list=[]
tuples=[]
for i in range(1, 4000, 1000):
    for j in range(1, 4000, 1000):
        print("__________________________NEW EXPERIMENT__________________________")
        print("Window: " + str(i))
        print("Lookahead: " + str(j))
        start = 0
        start = time.time()
        compress("../sample_img.jpg", j, i)
        ratio1=get_ratio()
        finish = time.time()
        aferesi=finish-start
        print("Time taken = " + str(aferesi))
        tuples.append([i,j,aferesi])
        time_list.append(aferesi)
        window_size.append(i)
        buffer_size.append(j)
        ratio.append(ratio1)


print("max time: ", max(time_list))
print("min time: ", min(time_list))
index_max=time_list.index(max(time_list))
index_min=time_list.index(min(time_list))
print("window max: " , window_size[index_max])
print("buffer max: " , buffer_size[index_max])
print("window min: " , window_size[index_min])
print("buffer min: " , buffer_size[index_min])
print(tuples)


sep = ""
with open('my.csv', 'w') as csv:
    for row in tuples:
        csv.write(sep.join(str(row)))
        csv.write("\n")


"""
print("max ratio: ", max(ratio))
index=ratio.index(max(ratio))
print("window: " , window_size[index])
print("buffer: " , buffer_size[index])
"""
