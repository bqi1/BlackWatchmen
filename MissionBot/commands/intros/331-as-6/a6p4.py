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
Problem 4
"""

from sys import flags
import a6p1, a6p3, a5p1, re

def breakSub( ciphertext: str, textFile: "str path to a text file", n: int ) -> str:
    mapping = a5p1.freqDict(ciphertext) # Call assignment 5's frequency dict method to get an initial mapping
    new_mapping = mapping.copy()
    n_gram_freq_dict = a6p1.ngramsFreqsFromFile(textFile,n) # Get all n-grams of text file in a frequency dictionary
    while True:
        # Keep iterating until we have the best unchanged mapping
        new_mapping = a6p3.bestSuccessor(mapping,ciphertext,n_gram_freq_dict,n)
        if new_mapping == mapping:
            break
        else:
            mapping = new_mapping.copy()
    # Call assignment 5's frequency decrypt, which maps a ciphertext to a given mapping.
    return a5p1.freqDecrypt(new_mapping,ciphertext)

        
def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    pass


    
if __name__ == "__main__" and not flags.interactive:
    test()
