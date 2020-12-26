# main method for testing functions

# import sys
# from os import path
# sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))

# from dna_toolset.dna_toolkit import * # REMOVES UNDERLINE ISSUE BUT DOESN'T WORK!
from dna_toolkit import * # LOCAL PATH WORKS FINE BUT IDE THINKS IT'S PROBLEMATIC

# ===== Part 1 =====

valid_DNA_strand_1 = "ATTTCGT"
print(validate_sequence(valid_DNA_strand_1)) # True

valid_DNA_strand_2 = "attcgta"
print(validate_sequence(valid_DNA_strand_2)) # True

invalid_DNA_strand = "ATTXCGT"
print(validate_sequence(invalid_DNA_strand)) # False

random_DNA_strand = generate_random_DNA_string(10)
print(random_DNA_strand) # GGTGTACTGT

print(count_nucleotide_frequency(random_DNA_strand)) # {'A': 1, 'C': 1, 'G': 4, 'T': 4}

print(optimised_count_nucleotide_frequency(random_DNA_strand))

print(nucleotide_percentage_frequency(random_DNA_strand)) # {'A': 10.0, 'C': 10.0, 'G': 40.0, 'T': 40.0}

random_DNA_strand_2 = generate_random_DNA_string(1000)
print(nucleotide_percentage_frequency(random_DNA_strand_2))

# ===== Part 2 =====

print(transcription(random_DNA_strand))

print(random_DNA_strand)
print(reverse_complement(random_DNA_strand))

show_full_sequence(random_DNA_strand)