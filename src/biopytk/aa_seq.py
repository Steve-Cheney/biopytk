# FASTA Toolkit
# Last updated: 8/30/23
#
# This module contains Amino Acid & Polypeptide analysis tools.
#
# Classes included in this file:
#   - sequenceBuilder
#   - structs
#
# https://www.stephendoescomp.bio
# Stephen Cheney © 2023

from structs import *
from sequenceBuilder import *

class aa_seq():
    def __init__(self, seq = "FLIMSY", label = 'No Label'):
        self.seq = seq.upper()
        self.seq_type = 'AA'
        self.label = label
        self.is_valid = self.validateSeq()
        assert self.is_valid, f"Input AA sequence is invalid: {self.seq}"


    def validateSeq(self):
        """
        Return True if input sequence is a valid AA sequence, return False otherwise
        \n<- bio_seq obj
        \n-> bool
        """
        return set(codons.values()).issuperset(self.seq)


    def getProteinsFromRF(amino_acid_seq):
        """
        Given an amino acid sequence, return all possible proteins
        \n<- amino_acid_seq: chr[]
        \n-> str[]
        """    
        curr_protein = ""
        proteins = []

        for each in amino_acid_seq:
            if each == "_":
                if bool(curr_protein):
                    proteins.append(curr_protein)
                    curr_protein = ""
            else:
                if each == "M":
                    curr_protein += each
                elif bool(curr_protein):
                    curr_protein += each
        if bool(curr_protein):
            proteins.append(curr_protein)
            curr_protein = ""
        return proteins