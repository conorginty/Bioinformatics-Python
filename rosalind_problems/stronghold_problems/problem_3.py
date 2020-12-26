# Complementing a Strand of DNA

# Problem
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string s of length at most 1000 bp.

# Return: The reverse complement sc of s.

# To access the code from the dna_toolset folder
import sys
sys.path.insert(1, '/Users/conorginty/Desktop/Bioinformatics_in_Python/dna_toolset')

from dna_toolkit import reverse_complement

s = "AAAACCCGGT"

rev_comp_s = reverse_complement(s)
print(rev_comp_s) # ACCGGGTTTT