# main method for testing functions

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))

# path_of_interest = path.dirname(path.dirname(path.realpath(__file__)))
# print(path_of_interest)

from dna_toolset.dna_toolkit import * # REMOVES UNDERLINE ISSUE BUT DOESN'T WORK!
# from dna_toolkit import * # LOCAL PATH WORKS FINE BUT IDE THINKS IT'S PROBLEMATIC

from dna_toolset.decorate import *

# ===== Part 1 =====
part_header("Part 1")

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
part_header("Part 2")

print(transcription(random_DNA_strand))

print(random_DNA_strand)
print(reverse_complement(random_DNA_strand))

show_full_sequence(random_DNA_strand)

# ===== Part 3 =====
part_header("Part 3")

test_DNA_strand = "ATTC"

print(f"{gc_content(test_DNA_strand)}%")

test_DNA_strand = "ATTCG"

print(f"{gc_content(test_DNA_strand)}%")

random_DNA_strand_3 = generate_random_DNA_string(50)
print(random_DNA_strand_3)
print(gc_content_subsection(random_DNA_strand_3, 5))

# ===== Part 4 =====
part_header("Part 4")

random_DNA_strand_4 = generate_random_DNA_string(21)
print(random_DNA_strand_4)
print(translate_sequence(random_DNA_strand_4))

sample_amino_acid_list = ["C", "S", "F", "V", "_", "A", "R"]
for aa in sample_amino_acid_list:
    print(f'Currently checking for {aa}:\n {codon_usage(random_DNA_strand_4, aa)}')

# ===== Part 5 =====
part_header("Part 5")

print(random_DNA_strand_4)
for frame in generate_reading_frames(random_DNA_strand_4):
    print(frame)

# ===== Part 6 =====
part_header("Part 6")

random_DNA_strand_5 = generate_random_DNA_string(198)
first_frame = generate_reading_frames(random_DNA_strand_5)[0]
print("first_frame", first_frame)
print(search_proteins_in_reading_frame(first_frame))

# ===== Part 7 =====
part_header("Part 7")

for protein in read_all_proteins_from_orfs(random_DNA_strand_5, 0, 0, True):
    print(protein)
print("---")

# Human Insulin
for protein in read_all_proteins_from_orfs(human_insulin, 0, 0, True):
    print(protein)