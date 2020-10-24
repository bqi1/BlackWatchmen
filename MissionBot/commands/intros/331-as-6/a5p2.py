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
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def evalDecipherment(text1: str, text2: str) -> [float, float]:
    # Assume that the substitution is 1-1 mapping; No cipher letter can be mapped to more than 1 plain text letter and vice versa
    plain_tokens = [] # Contains all unique tokens in plaintext, in an ordered list.
    deciphered_tokens = [] # Contains all unique tokens in deciphered text, in an ordered list
    correct = 0 # How many tokens are correctly matched against each other
    # Fill plain_tokens with all unique tokens
    for letter1, letter2 in zip(text1,text2):
        if letter1.upper() not in plain_tokens and letter1.upper() in LETTERS:
            plain_tokens.append(letter1.upper())
            deciphered_tokens.append(letter2.upper())
    # Compare tokens to see if they match each other
    for p_letter, d_letter in zip(plain_tokens,deciphered_tokens):
        if p_letter == d_letter:
            correct += 1
    key_accuracy = correct/len(plain_tokens)
    




    # Compare letters with each other. If it's a match, then increase correct
    letter1NoPunct = [x for x in text1 if x.upper() in LETTERS]
    letter2NoPunct = [x for x in text2 if x.upper() in LETTERS]
    length = 0
    correct = 0
    for letter1,letter2 in zip(letter1NoPunct,letter2NoPunct): # Compare texts letter by letter
        if letter1.upper() in LETTERS and letter2.upper() in LETTERS: # First check if it's a letter before counting it as valid
            length += 1
            if letter1.upper() == letter2.upper(): # If correctly matched, increment correct
                correct += 1
    if length != 0:
        decipherment_accuracy = correct/length
    else:
        decipherment_accuracy = 0

    print(f"Key accuracy: {key_accuracy}\tDecipherment accuracy: {decipherment_accuracy}")
    return [key_accuracy,decipherment_accuracy]
def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    # print(evalDecipherment("this is an examPle","tsih ih an ezample"))

if __name__ == '__main__' and not flags.interactive:
    test()
