from random import random

from parser import Object


def add_random_predicate(ind):
    pass

def remove_random_predicat(ind):
    pass

def mutate_pop(pop, p=.05) -> list[Object]:
    for individual in pop:
        if random() < p:
            remove_random_predicat(individual.predicate)
        if random() < p:
            add_random_predicate(individual.predicate)
        #TODO
        pass

    return pop