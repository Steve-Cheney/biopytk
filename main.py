# Computational Biology Python Tools
# Last updated: 8/15/23
#
#
# Packages included in this file:
#   - dnaToolkit.py
#
# https://www.stephendoescomp.bio
# Stephen Cheney © 2023

from dnaToolkit import *
import random

class main:
   
    
    dnaStr = cleanSeq(randDNASeq(10))
    dnaStr2 = cleanSeq(randDNASeq(100))

    #print(dnaStr)
    print(printBasePairs(dnaStr))
    #print(translate(transcribe(reverseCompliment(dnaStr))))
    #print(randPolyPeptide(5))

    

main()

