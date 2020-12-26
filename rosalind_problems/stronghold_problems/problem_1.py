# Counting DNA Nucleotides

# Problem
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string s of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

def rosalind_problem_1(dna_sequence):
    '''Returns the counts of each of the nucleotides in the DNA sequence'''
    
    nucleotide_counts = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0
    }
    
    for nucleotide in dna_sequence:
        nucleotide_counts[nucleotide] += 1
    
    for value in nucleotide_counts.values():
        print(value, end=" ")
    print()

rosalind_problem_1("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")