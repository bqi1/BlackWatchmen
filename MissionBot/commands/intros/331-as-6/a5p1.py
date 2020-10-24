#!/usr/bin/env python3

#---------------------------------------------------------------
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
#---------------------------------------------------------------

"""
Subsititution cipher frequency analysis
"""
from sys import flags
from collections import Counter # Helpful class, see documentation or help(Counter)

ETAION = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def freqDict(ciphertext: str) -> dict:

    """
    Analyze the frequency of the letters
    """
    occurence_mapping = {}
    # First map letters to how many times they appear in the ciphertext. For example, "AAAA" will have "A":4 in the occurence_mapping
    for letter in LETTERS:
        occurence_mapping[letter] = 0
    for letter in ciphertext:
        if letter.upper() in LETTERS:
            if letter.upper() not in occurence_mapping.keys():
                occurence_mapping[letter.upper()] = 1
            else:
                occurence_mapping[letter.upper()] += 1

    # Now map letters to their plaintext given by frequency in ETAION. If two or more letters have the same value, order them occording to when they first appeared
    letter_mapping = {} # Maps letters to most frequent plaintext in ETAION
    index = 0 
    # Iterate through all letters in ETAION until we have went through all occurences
    while True:
        if len(occurence_mapping) == 0 or index >= len(ETAION):
            break
        # Get the highest occuring letter in the occurence_mapping in a list
        max_occurence = max(occurence_mapping.values())
        letters = [key for key,value in occurence_mapping.items() if value == max_occurence]
        
        if len(letters) > 1: # If there are more than two letters with the same amount of occurences:
            ordering = resolve_tie(letters, ciphertext) # Retrieve a list of the proper ordering
            # For each ordered letter, assign it to the very next letter in ETAION. Delete the letter from the occurence_mapping to know we have passed over it.
            for ordered_letter in ordering:
                letter_mapping[ordered_letter] = ETAION[index]
                del occurence_mapping[ordered_letter]
                index+=1
        else: # There is only one letter with a certain amount of maximum occurences
            letter_mapping[letters[0]] = ETAION[index]
            del occurence_mapping[letters[0]] # Remove the letter from occurence_mapping to know we passed it
            index+=1

    letter_mapping[" "] = " "
    return letter_mapping

def freqDecrypt(mapping: dict, ciphertext: str) -> str:
    """
    Apply the mapping to ciphertext
    """
    # Replace each letter with the mapping's value, accounting for whether it's upper or lower case
    decrypted = list(ciphertext)
    for index in range(len(ciphertext)):
        if ciphertext[index] in LETTERS:
            if ciphertext[index].isupper():
                decrypted[index] = mapping[ciphertext[index]]
            else:
                decrypted[index] = mapping[ciphertext.upper()].lower()
    return ''.join(decrypted)

def resolve_tie(letters: list, ciphertext: str) -> list:
    """
    Given two or more letters in a list, resolve the ordering by analyzing the first occurences of each letter
    """
    first_occurences = {} # Map letters to the very first index they appear in ciphertext. For example, if ciphertext is "ABCDABCD," then "B" would map to 1 
    ordering = [] # Return list of ordered letters
    for letter in letters:
        first_occurences[letter] = ciphertext.upper().find(letter)
    while True: # Exhaust dictionary of first_occurences. Delete entries to know we evaluated them
        if len(first_occurences) == 0: break
        min_index = min(first_occurences.values()) # Find the first occuring index. The letter will be appended first to ordering.
        leftmost_key = [key for key,value in first_occurences.items() if value == min_index][0] # Find the letter corresponding to the first occuring index
        ordering.append(leftmost_key)
        del first_occurences[leftmost_key]

    return ordering

def test():
    "Run tests"
    # assert type(freqDict("A")) is dict
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    message = "AAABCCDDA A"
    mapping = freqDict(message)
    print(mapping)

# Invoke test() if called via `python3 a5p1.py`
# but not if `python3 -i a5p1.py` or `from a5p1 import *`
if __name__ == '__main__' and not flags.interactive:
    test()
