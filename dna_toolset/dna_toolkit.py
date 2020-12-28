# DNA Toolkit

# ===== Part 1 =====
# TO BE ABLE TO IMPORT FROM ANY FOLDER

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))

# NOT SURE HOW TO SUIT BOTH SCENARIOS BELOW (path problem...);
# ============================================================
# 1. Needed for problem_2.py
from dna_toolset.structures import *
# 2. Needed for main.py
# from structures import *

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

# ===== Part 2 =====

def transcription(dna_sequence):
    '''Replace any occurences of Thymine with Uracil then return the sequence'''
    # DNA -> mRNA
    return dna_sequence.replace("T", "U")

def reverse_complement(dna_sequence):
    '''returns the complement sequence to a given DNA strand
    A - T (2 H Bonds)
    C - G (3 H Bonds)
    '''
    
    # === Version 1 ===
    # # Get the complement for each Nucleotide
    # complement = ''.join(dna_reverse_complement[nucleotide] for nucleotide in dna_sequence)
    
    # # Reverse the Complement strand
    # reverse_complement = complement[::-1]
    
    # return reverse_complement

    # === Version 2: Faster, More Pythonic Approach ===
    # VERY specific for Python
    mapping = str.maketrans("ATCG", "TAGC")
    return dna_sequence.translate(mapping)[::-1]

def show_full_sequence(dna_sequence, reverse=True):
    '''Creates Representation of a DNA based one one of the strands'''
    
    connections = "|" * len(dna_sequence)
    
    if reverse:
        complement_opposite_direction = reverse_complement(dna_sequence)[::-1]
    else:
        complement_opposite_direction = reverse_complement(dna_sequence)
    
    print(f"5' {dna_sequence} 3'")
    print("  ", connections)
    print(f"3' {complement_opposite_direction} 5'")

# ===== Part 3 =====

def gc_content(dna_sequence):
    '''Returns the GC content in a nucleic acid sequence (either DNA or RNA)'''
    return round( (dna_sequence.count("C") + dna_sequence.count("G")) / len(dna_sequence) * 100)

def gc_content_subsection(dna_sequence, k):
    '''Returns the GC content in a nucleic acid (either DNA or RNA) sequence in subsections of length k (our window)'''

    result = []

    for i in range(0, len(dna_sequence)-k+1, k):
        sub_sequence = dna_sequence[i: i+k]
        # calculate the GC content of the window
        result.append(gc_content(sub_sequence))
    return result