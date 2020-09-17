#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
	return 0 == len(string)%2


def get_num_char(string, char):
	total =0
	for lettre in string:
		total += 1*(lettre == char)
	return total


def get_first_part_of_name(name):
	firstname = name.split("-",1)
	firstname[0]= firstname[0].capitalize()
	return "Bonjour, " + firstname[0]


def get_random_sentence(animals, adjectives, fruits):
	rndAnimal = animals[random.randrange(0,len(animals))]
	rndAdjective = adjectives[random.randrange(0,len(adjectives))]
	rndFruit = fruits[random.randrange(0,len(fruits))]

	return f"Aujourd’hui, j’ai vu un {rndAnimal} s’emparer d’un panier {rndAdjective} plein de {rndFruit}."


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
