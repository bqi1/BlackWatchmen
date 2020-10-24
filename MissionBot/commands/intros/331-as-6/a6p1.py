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
Problem 1
"""

from sys import flags
import re

def ngramsFreqsFromFile(textFile: "str path to a text file", n: int) -> dict:
    n_grams = {} # Dictionary of n-grams to return
    num_n_grams = 0 # Number of n-grams
    with open(textFile,encoding='utf-8') as my_file: # Read the file and retrieve its contents
        text = my_file.read().replace('\n', '').upper()
        for i in range(len(text)):
            # Go through the file's content letter by letter. On each letter, go up from that letter to n letters.
            temp_n_gram = text[i:i+n].upper()
            # If temporary n-gram does not match n characters, skip over it. This means we're nearing the end of the file.
            if len(temp_n_gram) == n:
                # If already existing, add 1 to its occurence, else initialize it as occuring once
                num_n_grams += 1
                if temp_n_gram in n_grams:
                    n_grams[temp_n_gram] += 1
                else:
                    n_grams[temp_n_gram] = 1
            else:
                break
    for key in n_grams:
        n_grams[key] /= num_n_grams # Calculate frequency for each distinct n_gram
    return n_grams


def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    # for x in range(1,6):
    #     print(ngramsFreqsFromFile('test.txt',x))
    print(ngramsFreqsFromFile('wells.txt',3))

if __name__ == "__main__" and not flags.interactive:
    test()
