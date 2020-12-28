# Computing GC Content

# Problem
# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

# ===== TO BE ABLE TO IMPORT FROM ANY FOLDER ===== 
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))
# print(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))

# ==== Version 1: ====

# Steps;
# 1. Read data from a FASTA-formatted file
def read_file_lines_into_list(file_path):
    '''Read a file and return as a list of lines'''
    with open(file_path, "r") as f:
        # Convert each line to a list entry
        return [line.strip() for line in f.readlines()]

def gc_content(dna_sequence):
    '''Returns the GC content in a nucleic acid sequence (either DNA or RNA)'''
    return round( (dna_sequence.count("C") + dna_sequence.count("G")) / len(dna_sequence) * 100)

# 2. Covert data from file into format that can be processed by our function (i.e. concat each line that makes up a DNA strand)

# Store input file contents in a list
FASTA_file_as_list = read_file_lines_into_list("rosalind_problems/stronghold_problems/input_files/fasta_eg.txt")
print(FASTA_file_as_list)
print(len(FASTA_file_as_list)) # 33

# Dictionary for Labels (keys) and Data (values)
FASTA_dict = {}

# Converting FASTA_file_as_list into a dictionary
for line in FASTA_file_as_list:
    if line[0] == ">":
        # Store current Label and make it a key
        FASTA_label = line
        FASTA_dict[FASTA_label] = ""
    else:
        FASTA_dict[FASTA_label] += line

print(FASTA_dict)
print(len(FASTA_dict)) # 2

# 3. Determine GC Content of each dictionary entry

# Using Dictionary Comprehension to generate a new dictionary with GC Content
result_dict = {key: f"{gc_content(value)}%" for (key, value) in FASTA_dict.items()}
print(result_dict) # {'>HSBGPG Human gene for bone gla protein (BGP)': '64%', '>HSGLTH1 Human theta 1-globin gene': '70%'}

# 4. Determine entry with highest GC Content

# Testing to understand the syntax of the max() function in combo with the key arg...
test = {
    "a": 1,
    "b": 10,
    "c": 5,
}

max_test = max(test, key=test.get) # dict.get when used in max() collects all the values in the dict, then we get the max of them
print(max_test)

max_gc_content = max(result_dict, key=result_dict.get)
print(max_gc_content)

# 5. Rosalind Submission

print(f'{max_gc_content[1:]}\n{result_dict[max_gc_content]}')