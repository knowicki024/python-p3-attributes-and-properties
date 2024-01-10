#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Fido", breed="Mastiff"):
        self._name = name
        self._breed = breed
        if not self._is_valid_name(name):
            print("Name must be string between 1 and 25 characters.")
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if self._is_valid_name(value):
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
    
   
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
    

    def _is_valid_name(self,value):
        return isinstance(value, str) and 1 <= len(value) <= 25
    

my_dog = Dog("Fido", "Mastiff")
print(my_dog.name)  


