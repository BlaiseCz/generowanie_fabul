from world import World
from random import random

def init_pop(pop_size=100) -> list(World):
    population = list()
    for id in range(pop_size):
        world = World(id)
        world.read_from_xml('./geneticquest_db.xml')
        population.append(world)
        print(f"World #{world.id} created")

    return population

def mutate_member(member, p=0.1):
    if p < random():
        member.add_random_goal()
    if p < random():
        member.remove_random_goal()

    return member


def calc_fitness(sollution):
    pass


def assign_fitness(pop):
    # load sollutions.all file, then assign proper fitness
    # load file
    loaded_file = [] #TODO
    for individual in pop:
        individual.calculate_fitness(loaded_file[individual.id])

    pass


def remove_worst_from_pop(last):
    pass


def add_new_members(pop):
    pass