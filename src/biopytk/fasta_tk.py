# FASTA Toolkit
# Last updated: 8/30/23
#
# This module contains FASTA file analysis tools. 
#
# Classes included in this file:
#   - sequenceBuilder
#   - structs
#   - bio_seq
#
# https://www.stephendoescomp.bio
# Stephen Cheney © 2023

from structs import *
from sequenceBuilder import *
from bio_seq import *
from aa_seq import *


def percentGC_fasta(seq):
    """
    Return GC percentage of a DNA sequence in % form
    \n<- bio_seq obj
    \n-> float
    """
    temp_seq = bio_seq(seq)
    bases = len(seq)
    return float(temp_seq.nucFrequencyDict()['G']/bases * 100) + float(temp_seq.nucFrequencyDict()['C']/bases * 100)


def gcContentFromFASTA(fasta_File):
    """
    Given a FASTA file, return a dict of sequence names and their respective GC content
    \n<- fasta_File: FASTA formatted file 
    \n-> dict
    """
    seqDict = seqsFromFASTA(fasta_File)
    gcDict = {k:percentGC_fasta(v) for k,v in seqDict.items()}
    return gcDict


def getMaxGCFromFASTA(fasta_File):
    """
    Given a FASTA file, return the sequence with the largest GC content
    \n<- fasta_File: FASTA formatted file 
    \n-> dict
    """    
    gcDict = gcContentFromFASTA(fasta_File)
    maxKey = max(gcDict, key=gcDict.get)
    return {maxKey:gcDict[maxKey]}


def parseFASTA(fasta_File, labels = [], seq_type = 'AA'):
    """
    Parse a FASTA file into bio_seq or aa_seq objects
    \nNotes: seqs empty by default returns all sequences, otherwise returns list of bio_seq objects that match label in labels
    \n\tseq_type specifies what sequence type the function should interpret the FASTA file as. Default to amino acid/protein sequence.
    \n<- fasta_File: FASTA formatted file, labels: str[],  
    \n-> bio_seq[]
    """
    seqDict = seqsFromFASTA(fasta_File)
    if not bool(seqDict):
        return [] # Empty dict, no seqs
    
    if not bool(labels):
        if seq_type == 'AA':
            seqs = [aa_seq(v,k) for k,v in seqDict.items()]
        else:
            seqs = [bio_seq(v,seq_type,k) for k,v in seqDict.items()]
    else:
        if seq_type == 'AA':
            seqs = [aa_seq(v,k) for k,v in seqDict.items() if k in labels]
        else:
            seqs = [bio_seq(v,seq_type,k) for k,v in seqDict.items() if k in labels]
    
    return seqs
    