
import sys
import re

ic = int(sys.argv[1])

with open(sys.argv[2]) as asidstory:
    i = 0
    for line in asidstory:
        # ignore 1st line
        if i>0: 
            bar = re.search("^\s*$", line)
            if bar:
                # end with first empty line
                break
            foo = line.split()
            if len(foo) < 9: 
                continue
            start_ic = int(foo[-3])
            end_ic = int(foo[-1])
            if start_ic <= ic and ic <= end_ic:
                print (line, end="")
        i += 1
