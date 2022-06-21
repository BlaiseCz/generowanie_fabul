from copy import deepcopy

from typing import List
import numpy as np
import re

from world import World
from random import random, sample


def init_pop(pop_size=100) -> list:
    population = list()
    for id in range(pop_size):
        world = World(id)
        world.read_from_xml('./geneticquest_db.xml')
        world.add_random_goal()
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

def get_tensions(solutions_path, actions, population) -> List[World]:
    """
    Read planner output ("solutions.all") and get tensions for equivalent individual
    """
    actions_tension = {action.name: action.tension for action in actions}
    indv_idx = 0
    indv_tension = [0]
    with open(solutions_path) as solutions:
        for i, line in enumerate(solutions):
            process_line = re.sub("[()]","", line.lower()).split(" ")
            if i != 0 and process_line[0] == f"zombie{indv_idx + 2}\n":
                population[indv_idx].tension = indv_tension[1:]
                indv_tension = [0]
                indv_idx += 1
            if process_line[0] in actions_tension.keys():
                readed_tension = actions_tension[process_line[0]]
                new_tension = indv_tension[-1] + readed_tension
                indv_tension.append(new_tension)
    population[indv_idx].tension = indv_tension[1:] #handle last pop

    return population

def assign_fitness(member, desired_story_arc):
    def scale_tension(tension: List[int], interval: int) -> List[int]:
        return [tension[int(round((((i - 1) / interval) * (len(tension) - 1)) + 1)) - 1]
                for i in range(interval)]

    tensions = member.get_tensions()
    scaled_tensions = scale_tension(tensions, len(desired_story_arc))

    mse = (sum([(scaled_tensions[i] - desired_story_arc[i]) ** 2
                for i in range(len(desired_story_arc))]) / len(desired_story_arc))
    return len(member.actions_from_planner) / mse



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
def add_new_members(population, pop_size) -> List[World]:
    old_pop = deepcopy(population)
    while pop_size > len(population):
        ind_1, ind_2 = sample(old_pop, 2)
        population.append(ind_1 * ind_2)

    return population

""""""
def print_pop_stats(population):
    best = max(population, key=lambda ind: ind.fitness)
    mean = np.mean([c.fitness for c in population])
    std = np.std([c.fitness for c in population])
    print(f" max fitness: #{best.id} {best.fitness}")
    print(f" mean: {mean}")
    print(f" std: {std}")

