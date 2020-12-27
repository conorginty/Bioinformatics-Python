# Transcribing DNA into RNA

# Problem
# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

# Given: A DNA string t having length at most 1000 nt. (nt = nucleotides)

# Return: The transcribed RNA string of t.

# To access the code from the dna_toolset folder
import sys

# Version 1
# sys.path.insert(1, '/Users/conorginty/Desktop/Bioinformatics_in_Python/dna_toolset')

# Version 2
from os import path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))

path_of_interest = path.dirname(path.dirname(path.dirname(path.realpath(__file__))))
print(path_of_interest)

from dna_toolset.dna_toolkit import transcription

print(transcription("GATGGAACTTGACTACGTAAATT")) # GAUGGAACUUGACUACGUAAAUU