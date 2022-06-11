from copy import deepcopy

from typing import List

from world import World
from random import random, sample


def init_pop(pop_size=100) -> list:
    population = list()
    for id in range(pop_size):
        world = World(id)
        world.read_from_xml('./geneticquest_db.xml')
        population.append(world)
        print(f"World #{world.id} created")

    return population


def mutate_member(member, p=0.1):
    if random() < p:
        member.add_random_goal()
    if random() < p:
        member.remove_random_goal()

    return member


def calc_fitness(sollution):
    pass


def assign_fitness(pop):
    pass  # TODO
    # load sollutions.all file, then assign proper fitness
    # load file
    # loaded_file = []
    # for individual in pop:
    #     individual.calculate_fitness(loaded_file[individual.id])


"""
    removing last individuals with lowest fitness,
    to make space for crossovered individuals
"""


def remove_worst_from_pop(pop, last=10) -> List[World]:
    return sorted(pop, key=World.get_fitness())[:-last]


"""
    in paper they use roulette, 
    here we pick randomly 2 parents from population 
    and make crossover between them
"""


def add_new_members(pop, pop_size) -> List[World]:
    old_pop = deepcopy(pop)
    while pop_size > len(pop):
        ind_1, ind_2 = sample(old_pop, 2)
        pop.append(ind_1 * ind_2)

    return pop
