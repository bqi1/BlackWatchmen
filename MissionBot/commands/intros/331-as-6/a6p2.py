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
Problem 2
"""

from sys import flags
import re
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
def keyScore( mapping: dict, ciphertext: str, frequencies: dict, n: int ) -> float:
    keyScore = 0
    deciphered_text = decipher(mapping,ciphertext) # Decipher ciphertext with given mapping
    deciphered_ngrams = get_n_grams(deciphered_text,n) # Get the n_grams of the decipherement above
    for n_gram in deciphered_ngrams: # Iterate through all n_grams in the frequencies dictionary, calculating the score
        if n_gram not in frequencies: continue
        n_occurences = calculate_occurences(n_gram,deciphered_text) # Calculate number of occurences of n-gram
        relative_freq = frequencies[n_gram] # relative frequency of n-gram
        keyScore += n_occurences*relative_freq # Sum multiplication of # occurences with relative frequency of all n-grams in the set.
    return keyScore
def get_n_grams(deciphered_text,n):
    # Gets all n_grams of the deciphered text.
    n_grams = []
    for i in range(len(deciphered_text)):
        temp_n_gram = deciphered_text[i:i+n].upper()
        # If temporary n-gram does not match n characters, skip over it
        if len(temp_n_gram) == n:
            # If already existing, add 1 to its occurence, else initialize it as occuring once
            if not temp_n_gram in n_grams:
                n_grams.append(temp_n_gram)
    return n_grams
def calculate_occurences(n_gram: str, deciphered_text: str):
    # finditer() creates an iterable object of all occurences of a pattern/substring given a string. We use it to find the number of occurences the substring, n-gram, occurs in the deciphered text.
    return len(deciphered_text.split(n_gram))-1
def decipher(mapping: dict, ciphertext: str):
    # Apply mapping to ciphertext
    decrypted_message = list(ciphertext[:])
    for i in range(len(decrypted_message)):
        # For each letter in the ciphertext, change it to the mapping's corresponding value.
        index = LETTERS.index(decrypted_message[i].upper())
        decrypted_message[i] = mapping[LETTERS[index]]
    return "".join(decrypted_message)
def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    mapping = {"A":"Z","B":"Y","C":"X","D":"W","E":"V","F":"U","G":"T","H":"S","I":"R","J":"Q","K":"P","L":"O","M":"N","N":"M","O":"L","P":"K","Q":"J","R":"I","S":"H","T":"G","U":"F","V":"E","W":"D","X":"C","Y":"B","Z":"A"," ": " "}
    ciphertext = "AN EXAMPLE"
    frequencies = {'A': 0.2, 'N': 0.1, ' ': 0.1, 'E': 0.2, 'X': 0.1, 'M': 0.1, 'P': 0.1, 'L': 0.1}
    n = 1
    print(keyScore(mapping,ciphertext,frequencies,n))


if __name__ == "__main__" and not flags.interactive:
    test()





