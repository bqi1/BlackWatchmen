#!/usr/bin/env python3

# ---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2020 <<Brian Qi>>
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
# ---------------------------------------------------------------

"""
Problem 3
Version 1.2
"""
import a6p2, itertools
from sys import flags

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def bestSuccessor(mapping: dict, ciphertext: str, frequencies: dict, n: int) -> dict:
    best_mapping = mapping.copy() # Best_mapping is the mapping corresponding to the highest key score. Will be constantly updated with the best mapping.
    all_mappings = [] # A collection of all possible mappings
    # Iterate through all 2 pair alphabet permutations
    for r in itertools.product(LETTERS,LETTERS2):
        # If the new mapping dictionary is already in all_mappings, skip over it. For example, the swap "A and E" is the same as the swap "E and A"
        letter_x = r[0]
        letter_y = r[1]
        if letter_x == letter_y: continue # Don't swap a letter with itself.
        temp_mapping = mapping.copy()
        temp_letter = temp_mapping[letter_x][:]
        temp_mapping[letter_x] = temp_mapping[letter_y][:]
        temp_mapping[letter_y] = temp_letter[:]
        if temp_mapping not in all_mappings:
            all_mappings.append(temp_mapping.copy()) # Add the mapping
    best_score = a6p2.keyScore(best_mapping,ciphertext,frequencies,n) # Calculate the current best score.

    for temp_mapping in all_mappings: # For all new mappings, calculate the score and update the best_mapping when necessary. There are 325 mappings.
        score = a6p2.keyScore(temp_mapping,ciphertext,frequencies,n)
        if score > best_score: # If the score obtained is better than the best score, replace the best_score and best_mapping
            best_score = score
            best_mapping = temp_mapping
    return best_mapping


def breakKeyScoreTie(originalMapping, successorMappingA, successorMappingB):
    """
    Break the tie between two successor mappings that have the same keyscore

    originalMapping: mapping the the other parameters are successors to
    successorMappingA: mapping that has had two keys swapped
    successorMappingB: mapping that has had two other keys swapped

    Example usage:
    originalMapping = {"A": "A", "B": "B", "C": "C"}
    # Mapping with B and C switched
    successorMappingA = {"A": "A", "B": "C", "C": "B"}
    # Mapping with A and C switched
    successorMappingB = {"A": "C", "B": "B", "C": "A"}

    # AC < BC so this function will return successorMappingB
    assert breakKeyScoreTie(originalMapping, successorMappingA, successorMappingB) == successorMappingB

    """
    aSwapped = "".join(sorted(k for k, v in (
        set(successorMappingA.items()) - set(originalMapping.items()))))
    bSwapped = "".join(sorted(k for k, v in (
        set(successorMappingB.items()) - set(originalMapping.items()))))
    return successorMappingA if aSwapped < bSwapped else successorMappingB


def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    mapping = {"A":"Z","B":"Y","C":"X","D":"W","E":"V","F":"U","G":"T","H":"S","I":"R","J":"Q","K":"P","L":"O","M":"N","N":"M","O":"L","P":"K","Q":"J","R":"I","S":"H","T":"G","U":"F","V":"E","W":"D","X":"C","Y":"B","Z":"A"," ": " "}
    ciphertext = "AN EXAMPLE"
    frequencies = {'A': 0.2, 'N': 0.1, ' ': 0.1, 'E': 0.2, 'X': 0.1, 'M': 0.1, 'P': 0.1, 'L': 0.1}
    n = 1
    print(bestSuccessor(mapping,ciphertext,frequencies,n))
    assert breakKeyScoreTie({"A": "A", "B": "B", "C": "C"}, {"A": "A", "B": "C", "C": "B"}, {
                            "A": "C", "B": "B", "C": "A"}) == {"A": "C", "B": "B", "C": "A"}
    assert breakKeyScoreTie({"A": "A", "B": "B", "C": "C", "D": "D"}, {
                            "A": "B", "B": "A", "C": "C", "D": "D"}, {"A": "A", "B": "B", "C": "D", "D": "C"}) == {"A": "B", "B": "A", "C": "C", "D": "D"}


if __name__ == "__main__" and not flags.interactive:
    test()
