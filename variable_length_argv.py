import time

start = time.clock()

def sum(*argv):
    temp = 0
    for argu in argv:
        temp += argu
    return temp

print("Sum : %d" % (sum(29,67,3,1,100,2544,15485,5454,54545,1545,45,1545,54,55,4516,545)))
import os
print("Current working directory : "+str(os.getcwd()))
end = time.clock()

print("Exectuiton time in seconds : %.6f sec" % (end-start))