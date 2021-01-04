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

# ===== Part 4 =====

# Generate a DNA Codon Table
def translate_sequence(dna_sequence, init_pos=0):
    '''Translate a DNA Sequence into an Amino Acid Sequence'''
    # init_pos is used to generate reading frames
    # Read the sequence 3 nucleotides at a time, jumping 3 nucleotides each read
    return [dna_codons[dna_sequence[pos:pos+3]] for pos in range(init_pos, len(dna_sequence)-2, 3)]

def codon_usage(dna_sequence, amino_acid):
    '''Provides the frequency of each codon encoding a given Amino Acid in a DNA Sequence'''

    # If our sequence contains an AA of interest, append it to a list
    temp_list = []
    for i in range(0, len(dna_sequence)-2, 3):
        current_triplet = dna_sequence[i: i+3]
        if dna_codons[current_triplet] == amino_acid:
            temp_list.append(current_triplet)

    # Calculate the frequency of a given codon that coded for the AA of interest
    # (e.g. value of 1.0 means that all occurrences of the AA were coded by the exact same triplet every time)
    freq_dict = dict(collections.Counter(temp_list))
    total_weight = sum(freq_dict.values())
    for sequence in freq_dict:
        freq_dict[sequence] = round(freq_dict[sequence] / total_weight, 2)
    return freq_dict

# ===== Part 5 =====

def generate_reading_frames(dna_sequence):
    '''Generate the 6 reading frames of a DNA sequence, including the Reverse Complement'''

    reading_frames = [] # Will store our 6 reading frames

    # 1st translate DNA seq then append to our frames
    # Append 1st 3 reading frames (strand itself)
    for i in range(3):
        translated_sequence = translate_sequence(dna_sequence, i)
        reading_frames.append(translated_sequence)

    # Now append 2nd 3 reading frames (from complement strand)
    for i in range(3):
        translated_complement = translate_sequence(reverse_complement(dna_sequence), i)
        reading_frames.append(translated_complement)
    return reading_frames

# ===== Part 6 =====

def search_proteins_in_reading_frame(aa_sequence):
    '''Computes all possible proteins in an AA sequence and returns a list of possible proteins'''

    current_protein = [] # Accumulates our current protein (made up of AAs from M -> _)
    proteins = [] # # Accumulates all proteins generated

    for aa in aa_sequence:
        if aa == "_":
            # STOP codon - so stop appending list of proteins
            if current_protein: # If the current_protein list is NOT empty
                # For loop responsible for getting nested proteins (e.g. MAAMCG_ would produce: MAAMCG and MCG)
                for prot in current_protein:
                    proteins.append(prot)
                current_protein = []
        else:
            if aa == "M":
                # if START codon (M) - then start appending list of proteins
                current_protein.append("")
            # If the length of the current protein is > 0, build the protein 
            # Effectively gets skipped unless we've encountered a M already (so the length of current_protein will be at least 1 ("", "M", "MR" etc))
            for i in range(len(current_protein)):
                current_protein[i] += aa
    return proteins

