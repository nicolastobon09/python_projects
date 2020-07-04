#!/usr/bin/python3
""" Modules """
import random
import collections

""" Gobal Const """
PAL = ['espada', 'corazon', 'rombo', 'trebol']
VALUES = [
    'as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey'
    ]


def create_deck():
    """ Create """
    desks = []

    for palo in PAL:
        for value in VALUES:
            desks.append((palo, value))

    return desks


def get_hand(desk, size):
    """ get """
    hand = random.sample(desk, size)

    return hand


def main(size, tries):
    """ main """
    desk = create_deck()
    hands = []

    for _ in range(tries):
        hand = get_hand(desk, size)
        hands.append(hand)

    both = 0
    for hand in hands:
        value = []
        for card in hand:
            value.append(card[1])

        counter = dict(collections.Counter(value))
        for val in counter.values():
            if val == 2:
                both += 1
                break

    probability = both / tries
    print(f"The probability of getting a pair in a {size} card hand is: {probability}")


if __name__ == "__main__":
    size = int(input("How many decks will the hand be: "))
    tries = int(input("How many attempts to calculate the probability: "))
    main(size, tries)
