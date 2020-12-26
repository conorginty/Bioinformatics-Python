# DNA Toolkit

# ===== Part 1 =====
# TO BE ABLE TO IMPORT FROM ANY FOLDER

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))

from structures import *

import random
import collections

def validate_sequence(dna_sequence):
    '''Check the sequence of the input to verify it is a valid DNA sequence'''
    
    upper_case_seq = dna_sequence.upper()
    
    for nucleotide in upper_case_seq:
        if nucleotide not in nucleotides:
            return False
    return True


def generate_random_DNA_string(length_of_seq):
    '''Generate a random DNA sequence of input length'''
    
    # === Version 1 === 
#     random_DNA_string = ''.join([random.choice(nucleotides) for nucleotide in range(length_of_seq)])
    
    # === Version 2 === 
    random_DNA_string = ''
    for i in range(length_of_seq):
        random_DNA_string += random.choice(nucleotides)
    
    return random_DNA_string

def count_nucleotide_frequency(dna_sequence):
    '''Count frequencies of each nucleotide within a given DNA sequence'''

    nucleotide_counts = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0
    }
    
    for nucleotide in dna_sequence:
        nucleotide_counts[nucleotide] += 1
    
    return nucleotide_counts

# Optimising the count_nucleotide_frequency function with the collections module
# I THINK JUST IN TERMS OF FEWER LINES???
def optimised_count_nucleotide_frequency(dna_sequence):
    # Get the count, then cast the Counter object to a python dictionary
    return dict(collections.Counter(dna_sequence))

# ===== EXTRA (my idea) =====
def nucleotide_percentage_frequency(dna_sequence):
    '''Calculates the percentage of each Nucleotide in the DNA Sequence'''

    nucleotide_counts = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0
    }
    
    for nucleotide in dna_sequence:
        nucleotide_counts[nucleotide] += 1
    
    nucleotide_freqs = {}
    
    total_count = len(dna_sequence)
    
    # Calculating the frequency of each Nucleotide and adding it nucleotide_freqs
    for nucleotide_key in nucleotide_counts:
        nucleotide_freqs[nucleotide_key] = round(nucleotide_counts[nucleotide_key] / total_count * 100, 2)
    
    return nucleotide_freqs