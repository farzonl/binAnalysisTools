#!/usr/bin/python3

import sys, lief

def symbolStats(binary):
    symNames = []
    for symbol in binary.symbols:
        symNames.append( (symbol.name, "") )
    return symNames

def sectionStats(binary):
    rows = []
    for section in binary.sections:
        rows.append( (section.name, str(section.size)) )
    return rows

def  diffSecStats(binA, binB):
   rowA = sectionStats(binaryA)
   rowB = sectionStats(binaryB)
   rowsDiff = list(set(rowA) ^ set(rowB))
   rowsSim  = set(rowA).intersection(set(rowB))
   simLen = len(rowsSim)
   diffLen = len(rowsDiff)
   if len(rowsDiff) == 0:
       print("binaries are the same size for all sections")
       return
   rows =  [("sections", "size"),
            ("~~~~~~~~", "~~~~")]  + rowsDiff
   format(rows)
   print("binary sections is: %f %% similar" % (simLen / (simLen + diffLen)* 100) )

def  diffSymStats(binA, binB):
    rowA = symbolStats(binaryA)
    rowB = symbolStats(binaryB)
    rowsDiff = list(set(rowA) ^ set(rowB))
    rowsSim  = set(rowA).intersection(set(rowB))
    simLen = len(rowsSim)
    diffLen = len(rowsDiff)
    if len(rowsDiff) == 0:
        print("binaries are the same for all symbols")
        return
    rows =  [("symbols",""),
             ("~~~~~~~","")]  + rowsDiff
    format(rows)
    
    print("binary symbols is: %f %% similar" % (simLen / (simLen + diffLen) * 100) )
    

def format(rows):
    lens = []
    for col in zip(*rows):
        lens.append(max([len(v) for v in col]))
    format = "  ".join(["{:<" + str(l) + "}" for l in lens])
    for row in rows:
        print(format.format(*row))

if __name__ == "__main__":
   argc = len(sys.argv)

   if (argc < 3):
       print("need 2 arguments")
       exit(0)
   binaryA = lief.parse(sys.argv[1])
   binaryB = lief.parse(sys.argv[2])
   diffSecStats(binaryA,binaryB)
   diffSymStats(binaryA,binaryB)
   
