#!/usr/bin/python3
import re

def normalize(word):
    """ setting word """
    word.lower()
    pattern = r'[,|.|!]+?'

    return re.sub(pattern, "", word)

def findWord(sentence):
    """ Find a word repeated"""
    array_words = sentence.split()
    new_dict = {}

    for word in array_words:
        nor_word = normalize(word)

        if  nor_word in new_dict:
            new_dict[nor_word] += 1
        else:
            new_dict[nor_word] = 1

    return max(new_dict, key=new_dict.get)
    

if __name__ == "__main__":
    sentence = str(input("Write a sentence and I'll find the most repeated word: "))
    word = findWord(sentence)
    print(f'The word most repeated is: {word}')
