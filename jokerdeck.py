#!/usr/bin/env python

from carddeck import CardDeck

class Dog():
    def bark(self):
        print("Yip! Yip!")

    def drool(self):
        print("drooling!")

class JokerDeck(Dog, CardDeck):

    def _create_deck(self):
        super()._create_deck()

        self._cards.append((1, 'Joker'))
        self._cards.append((2, 'Joker'))


