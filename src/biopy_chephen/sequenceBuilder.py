# Sequence Builder
# Last updated: 8/15/23
#
# This package contains DNA sequence building tools. 
#
# Classes included in this file:
#   - sequenceBuilder
#
# https://www.stephendoescomp.bio
# Stephen Cheney © 2023

import random
from geneticConst import *
from dnaToolkit import *

def randDNASeq(n):
    """
    Return a random DNA sequence of given length
    \n<- n: int
    \n-> str
    """
    assert(type(n) == int)
    return ''.join([random.choice(nucleotides) 
                        for nuc in range(n)])


def randRNASeq(n):
    """
    Return a random RNA sequence of given length
    \n<- n: int
    \n-> str
    """
    assert(type(n) == int)
    return ''.join([random.choice(rnaNucleotides) 
                        for nuc in range(n)])


def randPolyPeptide(n):
    """
    Return a random polypeptide of given length
    \n<- n: int
    \n-> str
    """
    assert(type(n) == int)
    return 'M' + ''.join([random.choice(list(innerCodons.values())) 
                        for i in range(n)])


def seqsFromFASTA(fasta_File):
    """
    Given a FASTA file, return a dict of sequence names and their respective sequence
    \n Notes: Does not discriminate between DNA, RNA, or Nucleotide sequences
    \n\tReturns empty {} if no properly formatted FASTA sequences
    \n<- fasta_File: FASTA formatted file 
    \n-> dict
    """
    lines = readFile(fasta_File)
    fastaDict = {}
    tempSeqName = ''
    tempSeq = ''

    for line in lines:
        if line[0] == '>':
            fastaDict[tempSeqName] = tempSeq.rstrip()
            tempSeq = ''
            tempSeqName = line[1:].rstrip()
            fastaDict[tempSeqName] = ''
        else:
            tempSeq += line.rstrip()
    fastaDict[tempSeqName] = tempSeq.rstrip()
    # Remove empty values
    fastaDict.pop('')
    fastaDict = {k:v for k,v in fastaDict.items() if v != ''}
    return fastaDict


def readFile(file):
    """
    Given a file, read and return the list of lines
    \n<- file
    \n-> str[]
    """
    with open(file, type) as f:
            lines = f.readlines()
    return lines

# ====== Function Comment Template ======

    """
    Purpose of Function
    \nNotes: [notes]
    \n\t[more notes]    
    \n<- input: type
    \n-> type
    """