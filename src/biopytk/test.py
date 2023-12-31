# BioPyTK Tests
#
#
# Packages included in this file:
# 
#
# https://www.stephendoescomp.bio
# Stephen Cheney © 2023

from tqdm import tqdm
from time import sleep
from bio_seq import *
from aa_seq import *
from fasta_tk import *
from structs import *
from sequenceBuilder import *

class test:
    def unitTest(name, func, output):
        try:
            assert func == output
            print(f'{name} Passed')
            return 1
        except AssertionError:
            print(f'Test Failed for {name}')
            return 0
    def unitTest2(func, output):
        try:
            assert func == output
            print(f'{func.__name__} Passed')
            return 1
        except AssertionError:
            print(f'Test Failed for {func.__name__}')
            return 0
    
    test_dna = bio_seq("GGTTTCCATCGCATGTGCGCTCCGAGTCCCTTCCTGAGCACGTCAAGCGGGCCGTACGAGATCTATAGTTAGGTAGACAGCTGGTGCAAAGACTAACCCGGCTGGTCGTGAGGACCTTGGACGGACTGTCAAAGCCTCGTATGTCCTCACAAGCCAGATTAGTGGTCCTACCCCACATATAGGGTGCGTGACCGCTGGCTAAGCAATTTCTATGCAGGGAATGTTTCTTTCCCTTTGGTCGCGACACTACAGAGCCTCGGGACTTGACAGTAATGTTAATCAGTCAAACGCCCTGTGCTTAGGTCATACGCACATTCTTTAGACAACCTGATTGCTGACGAATTGGACACTTGGCAATTTCAGGCCGTTATCTCTATCCATATACACGGTTTTAAAAAGCTCAGGCACTCTAAAAGGTCAGGGGAACAAAGGTCTGTCGTATAGGCAACTTTCGTAGCCTCAGAGACTTCACGGGATATGCATTCACTGTAGTCACATTTTCTGGTATTCGCAGACCGGCTGGTAACTCTCAACTAGTTGTCTCGACACATAGAGCGTAAATCTGACATCTCGTCCCGAACTGCACACGTCGCTAGGTACCCAAGGCGTGTATGCGCCATAGTTCCCCTAGAGAACAGTTACATACGGATCTCGAGATCAAGAAGACTGAACAGCAACCCTTTTCGTACTTCTACTAGCAGAATCGTGGGCTCGGTCCTGGAATAACGAAAAGTTTCAGCAGTTCCACTTGGAGACAGGGGCTTTCTCTATTTGCAGAACATTGGCTTGTGCTGAACGATGCCATTAAGGGCGAGCTCCTAATGTCTTGCTACTATATTAACTATTCGGTACCCGGGCAGTTAGCTCGATTCAAAACAAAGTGATGGGACGAACGCAATCAACGTTGACACAGGTCCAAAGTGCAAAGTAGACCGTCAAGGTAGTAACAGC")
    #.getAllORFProteins(ordered = True), ['MWGRTTNLACEDIRGFDSPSKVLTTSRVSLCTSCLPNYRSRTARLTCSGRDSERTCDGN', 'MQGMFLSLWSRHYRASGLDSNVNQSNALCLGHTHIL', 'MASFSTSQCSANRESPCLQVELLKLFVIPGPSPRFC', 'MRHSSPREQLHTDLEIKKTEQQPFSYFY', 'MAHTRLGYLATCAVRDEMSDLRSMCRDN', 'MSCYYINYSVPGQLARFKTK', 'MDRDNGLKLPSVQFVSNQVV', 'MCAPSPFLSTSSGPYEIYS', 'MGRTQSTLTQVQSAK', 'MSSQARLVVLPHI', 'MLISQTPCA', 'MPLRASS', 'MHSL', 'MHIP', 'MFCK', 'MRWK', 'MCV', 'MET', 'MT', 'M', 'M']
    #x = unitTest('transcribe()', test_dna.transcribe().seq,  'GGUUUCCAUCGCAUGUGCGCUCCGAGUCCCUUCCUGAGCACGUCAAGCGGGCCGUACGAGAUCUAUAGUUAGGUAGACAGCUGGUGCAAAGACUAACCCGGCUGGUCGUGAGGACCUUGGACGGACUGUCAAAGCCUCGUAUGUCCUCACAAGCCAGAUUAGUGGUCCUACCCCACAUAUAGGGUGCGUGACCGCUGGCUAAGCAAUUUCUAUGCAGGGAAUGUUUCUUUCCCUUUGGUCGCGACACUACAGAGCCUCGGGACUUGACAGUAAUGUUAAUCAGUCAAACGCCCUGUGCUUAGGUCAUACGCACAUUCUUUAGACAACCUGAUUGCUGACGAAUUGGACACUUGGCAAUUUCAGGCCGUUAUCUCUAUCCAUAUACACGGUUUUAAAAAGCUCAGGCACUCUAAAAGGUCAGGGGAACAAAGGUCUGUCGUAUAGGCAACUUUCGUAGCCUCAGAGACUUCACGGGAUAUGCAUUCACUGUAGUCACAUUUUCUGGUAUUCGCAGACCGGCUGGUAACUCUCAACUAGUUGUCUCGACACAUAGAGCGUAAAUCUGACAUCUCGUCCCGAACUGCACACGUCGCUAGGUACCCAAGGCGUGUAUGCGCCAUAGUUCCCCUAGAGAACAGUUACAUACGGAUCUCGAGAUCAAGAAGACUGAACAGCAACCCUUUUCGUACUUCUACUAGCAGAAUCGUGGGCUCGGUCCUGGAAUAACGAAAAGUUUCAGCAGUUCCACUUGGAGACAGGGGCUUUCUCUAUUUGCAGAACAUUGGCUUGUGCUGAACGAUGCCAUUAAGGGCGAGCUCCUAAUGUCUUGCUACUAUAUUAACUAUUCGGUACCCGGGCAGUUAGCUCGAUUCAAAACAAAGUGAUGGGACGAACGCAAUCAACGUUGACACAGGUCCAAAGUGCAAAGUAGACCGUCAAGGUAGUAACAGC')
    #print(x)
    unitTest2(test_dna.transcribe.seq,  'GGUUUCCAUCGCAUGUGCGCUCCGAGUCCCUUCCUGAGCACGUCAAGCGGGCCGUACGAGAUCUAUAGUUAGGUAGACAGCUGGUGCAAAGACUAACCCGGCUGGUCGUGAGGACCUUGGACGGACUGUCAAAGCCUCGUAUGUCCUCACAAGCCAGAUUAGUGGUCCUACCCCACAUAUAGGGUGCGUGACCGCUGGCUAAGCAAUUUCUAUGCAGGGAAUGUUUCUUUCCCUUUGGUCGCGACACUACAGAGCCUCGGGACUUGACAGUAAUGUUAAUCAGUCAAACGCCCUGUGCUUAGGUCAUACGCACAUUCUUUAGACAACCUGAUUGCUGACGAAUUGGACACUUGGCAAUUUCAGGCCGUUAUCUCUAUCCAUAUACACGGUUUUAAAAAGCUCAGGCACUCUAAAAGGUCAGGGGAACAAAGGUCUGUCGUAUAGGCAACUUUCGUAGCCUCAGAGACUUCACGGGAUAUGCAUUCACUGUAGUCACAUUUUCUGGUAUUCGCAGACCGGCUGGUAACUCUCAACUAGUUGUCUCGACACAUAGAGCGUAAAUCUGACAUCUCGUCCCGAACUGCACACGUCGCUAGGUACCCAAGGCGUGUAUGCGCCAUAGUUCCCCUAGAGAACAGUUACAUACGGAUCUCGAGAUCAAGAAGACUGAACAGCAACCCUUUUCGUACUUCUACUAGCAGAAUCGUGGGCUCGGUCCUGGAAUAACGAAAAGUUUCAGCAGUUCCACUUGGAGACAGGGGCUUUCUCUAUUUGCAGAACAUUGGCUUGUGCUGAACGAUGCCAUUAAGGGCGAGCUCCUAAUGUCUUGCUACUAUAUUAACUAUUCGGUACCCGGGCAGUUAGCUCGAUUCAAAACAAAGUGAUGGGACGAACGCAAUCAACGUUGACACAGGUCCAAAGUGCAAAGUAGACCGUCAAGGUAGUAACAGC')
        

test()