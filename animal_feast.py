
#the dish must start and end with the same letters as the animal's name
#o prato deve começar e terminar com as mesmas letras do nome do animal
#chickadee is bringing chocolate cake


def feast(animal_name, dish):
	first_letter_animal = animal_name[0:1]
	last_letter_animal = animal_name[-1:]
	first_letter_dish = dish[0:1]
	last_letter_dish = dish[-1:]
	test = first_letter_dish == first_letter_animal and last_letter_dish == last_letter_animal
	return test

