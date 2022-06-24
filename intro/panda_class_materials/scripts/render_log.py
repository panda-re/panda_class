import sys
import fileinput
for line in fileinput.input():
    parts = line.split()
    c = int(parts[-1], 16)
    if c>0 and c<256:
        sys.stdout.write(chr(c))



        
