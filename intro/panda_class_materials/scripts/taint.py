import sys
import itertools
from google.protobuf.json_format import MessageToJson

from pandare.plog_reader import PLogReader

f = open("tcns", "w")
pcc = {}
with PLogReader(sys.argv[1]) as plr:
    for i,m in enumerate(plr):
        if m.HasField('tainted_instr'):
            if not m.pc in pcc:
                pcc[m.pc] = 0
            pcc[m.pc] += 1
            for tb in m.tainted_instr.taint_query:
                f.write("%d %d\n" % (m.instr, tb.tcn))

f.close()

pcs = list(pcc.keys())
pcs.sort()

for pc in pcs:
    print ("tainted instr @ pc=%x count=%d" % (pc, pcc[pc]))
    
