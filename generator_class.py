#!/usr/bin/env python


class Dogs():
    BREEDS = ['Saint Bernard', 'German Shepherd',
              "Shit-tzu", 'Bulldog', 'Labrador Retriever']

    def __init__(self):
        self._index = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self.BREEDS):
            current = self._index
            self._index += 1

            return self.BREEDS[current]
        else:
            raise StopIteration()

dog_gen = Dogs()

for dog in dog_gen:
    print(dog)
