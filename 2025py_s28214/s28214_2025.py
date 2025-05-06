#!/usr/bin/env python3

"""
Purpose:
    Generate a random DNA sequence in FASTA format,
    inserting the user's name at a random position without
    affecting nucleotide statistics.

Context:
    Educational script for bioinformatics courses to illustrate
    sequence generation, FASTA formatting, and simple statistics.
"""

import random  # For generating random nucleotides and insertion position

# ----------------------------------------
# 1. VALIDATE SEQUENCE LENGTH (IMPROVEMENT 1)
#    ORIGINAL:
#      length = int(input("Enter the sequence length: "))
#    MODIFIED:
#      - Prompt shows an example (e.g., 10)
#      - Accepts digits only
#      - Ensures a positive integer
# ----------------------------------------
while True:
    length_input = input("Enter the sequence length (e.g., 10): ")
    if not length_input.isdigit():
        print("Please enter a valid positive integer (digits only).")
        continue
    length = int(length_input)
    if length <= 0:
        print("Please enter a positive integer for the sequence length.")
        continue
    break

# ----------------------------------------
# 2. VALIDATE SEQUENCE ID (IMPROVEMENT 2)
#    ORIGINAL:
#      seq_id = input("Enter the sequence ID: ")
#    MODIFIED:
#      - Non-empty, non-whitespace-only
#      - Prompt shows an example (e.g., A123)
# ----------------------------------------
while True:
    seq_id = input("Enter the sequence ID (e.g., A123): ")
    if not seq_id.strip():
        print("Sequence ID cannot be empty.")
        continue
    break

# ----------------------------------------
# 3. VALIDATE DESCRIPTION (IMPROVEMENT 3)
#    ORIGINAL:
#      description = input("Provide a description of the sequence: ")
#    MODIFIED:
#      - Non-empty
# ----------------------------------------
while True:
    description = input("Provide a description of the sequence: ")
    if not description.strip():
        print("Description cannot be empty.")
        continue
    break

# ----------------------------------------
# 4. VALIDATE USER NAME (IMPROVEMENT 4)
#    ORIGINAL:
#      user_name = input("Enter your name: ")
#    MODIFIED:
#      - Non-empty
# ----------------------------------------
while True:
    user_name = input("Enter your name: ")
    if not user_name.strip():
        print("Name cannot be empty.")
        continue
    break

# ----------------------------------------
# 5. SEQUENCE GENERATION & NAME INSERTION (IMPROVEMENT 5)
#    ORIGINAL:
#      seq = ''.join(random.choice(...))
#      pos = random.randint(0, length)
#      seq = seq[:pos] + user_name + seq[pos:]
#    MODIFIED:
#      - Encapsulated in functions for reuse and clarity
# ----------------------------------------

def generate_random_sequence(length):
    """Return a random DNA sequence of the specified length."""
    return ''.join(random.choice(nucleotides) for _ in range(length))


def insert_name(seq, name):
    """Insert `name` at a random position within `seq`."""
    position = random.randint(0, len(seq))
    return seq[:position] + name + seq[position:]

# Prepare nucleotide list after functions for clarity
nucleotides = ['A', 'C', 'G', 'T']

# Generate and insert
sequence = generate_random_sequence(length)
sequence = insert_name(sequence, user_name)

# ----------------------------------------
# 6. CALCULATE STATISTICS
#    - Count A, C, G, T
#    - Compute percentages and CG ratio
# ----------------------------------------
count_A = sequence.count('A')
count_C = sequence.count('C')
count_G = sequence.count('G')
count_T = sequence.count('T')

total_bases = count_A + count_C + count_G + count_T

percent_A = count_A / total_bases * 100
percent_C = count_C / total_bases * 100
percent_G = count_G / total_bases * 100
percent_T = count_T / total_bases * 100
percent_CG = (count_C + count_G) / total_bases * 100

# ----------------------------------------
# 7. WRITE TO FASTA (IMPROVEMENT 6)
#    ORIGINAL:
#      with open(f"{seq_id}.fasta", 'w') ...
#    MODIFIED:
#      - Wrap lines at 60 chars for FASTA standard
# ----------------------------------------
filename = f"{seq_id}.fasta"
with open(filename, 'w') as fasta_file:
    fasta_file.write(f">{seq_id} {description}\n")
    for i in range(0, len(sequence), 60):
        fasta_file.write(sequence[i:i+60] + "\n")

# ----------------------------------------
# 8. DISPLAY RESULTS
# ----------------------------------------
print(f"The sequence was saved to the file {filename}")
print("Sequence statistics:")
print(f"A: {percent_A:.1f}%")
print(f"C: {percent_C:.1f}%")
print(f"G: {percent_G:.1f}%")
print(f"T: {percent_T:.1f}%")
print(f"%CG: {percent_CG:.1f}%")

