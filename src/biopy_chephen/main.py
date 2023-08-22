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
   
    
    dnaStr = 'ATCGTCA'
    print(dnaSummary(dnaStr))
    
    print(seqsFromFASTA('test.fasta'))


main()

