#!/usr/bin/python3


def is_palindrome(word):
    """
    checks if a word or phrase is palindrome
    """
    word = word.replace(" ", "")
    new_word = word.lower()

    return new_word == new_word[::-1]


def run():
    """ Run the code """
    word = str(input("Write a word or phrase: "))
    result = is_palindrome(word)
    if result is True:
        print(f"{word} is palindrome")
    else:
        print(f"{word} is no palindrome")


if __name__ == "__main__":
    run()
