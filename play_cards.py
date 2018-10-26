#!/usr/bin/env python
import types

from carddeck import CardDeck
from jokerdeck import JokerDeck

# CardDeck d1 = new CardDeck()
d1 = CardDeck('Steve')

print(d1)


print(d1.dealer)

try:
    d1.dealer = 4.73
except TypeError as err:
    print(err)

print(d1.dealer)

print(d1.get_dealer())

CardDeck.get_dealer(d1)

d1.shuffle()
# print(d1.cards)

hand = []
for i in range(5):
    card = d1.draw()
    hand.append(card)

print("Hand:", hand)

print(d1.get_suits())

print(CardDeck.get_suits())

d1.bark()

CardDeck.bark()
d1.bark()

def cat_noise(self):
    print("Meow meow")

CardDeck.meow = cat_noise

d1.meow()

def get_first_card(self):
    return self._cards[0]

d1.get_first_card = types.MethodType(get_first_card, d1)


c = d1.get_first_card()
print(c)

# del d1.get_first_card
delattr(d1, "get_first_card")


print(dir(d1))

s = getattr(d1, 'shuffle')

s()

#  getattr() hasattr()
#  setattr() delattr()

j1 = JokerDeck("Jimmy")
j1.shuffle()

print(j1.cards)

j1.bark()


print(JokerDeck.mro())
j1.drool()

print(len(d1))
print(j1)
print(d1)

foo = j1 + d1

print(foo)

